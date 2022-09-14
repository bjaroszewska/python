from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from statistics import mean
import re
from termcolor import colored
from babel.numbers import format_currency
import numpy as np
from datetime import date
import csv

maxPages = 5
today = str(date.today())
fileName = today + "_Ingatlan_2_room.csv"

def formatPrices(data):
    return str(mean(data))

def reject_outliers(data, m=2):
    dataArray = np.array(data)
    return  dataArray[abs( dataArray - np.mean( dataArray)) < m * np.std( dataArray)]

print(reject_outliers([12332.5]))

def getPriceFromMillion(text):
    price = re.search('[0-9.]+', text).group()
    return  float(price) * 1000000

def getPrice(text):
     return float(re.search('[0-9.,]+', text.replace(' ','')).group().replace(',',''))

def generateFile():
    
    headerList = ['city', 'district', ' Ft/m2 average', "Price average from (Ft)", "Price average  (Ft)", "Rent average from", "Rent price average per month  (Ft)", "Average return per year (%)"]
    try:
        with open(fileName, "x") as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=headerList)
            dw.writeheader()
    except OSError as e:
        print("already there")
# print(getPriceFromMillion("HUF 63.9 million"))
# print(getPrice("HUF 1,996,875/"))
# print(getPrice("HUF 160,000/month"))

def getPricePerSM(website):
    pricePerSM = []
    for each_div in website.find_all("div", class_="price--sqm"):
        price = each_div.get_text()
        pricePerSM.append(getPrice(price))
    return pricePerSM

def getTotalPrice(website):
    totalPrice = []
    for each_div in website.find_all("div", class_="price"):
        totalPrice.append(getPriceFromMillion(each_div.get_text()))
    return totalPrice

def getRentPrice(website):
    rentPrice = []
    for each_div in website.find_all("div", class_="price"):
        rentPrice.append(getPrice(each_div.get_text()))
    return rentPrice

def main():
    currentPage = 1
    rentPrice = []
    pricePerSM = []
    totalPrice = []
    city = ""
    district = ""
    city = input("Which city are you interested in? ").lower()
    if (city.lower()=='budapest'):
        district = input("Which district are you interested in? ")

    #calculate buy
    for x in range(maxPages):
        print("currentPage: " + str(currentPage))
        if district == "":
            url ="https://ingatlan.com/lista/elado+lakas+" + city + "+20-50-m2+2-2-szoba-alatt?page=" + str(currentPage)
        else: 
            url ="https://ingatlan.com/lista/elado+lakas+20-50-m2+" + district+ "-ker+2-2-szoba-alatt?page=" + str(currentPage)
        # print("url generated for buying: " + url)
        req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

        web_byte = urlopen(req, timeout=10).read()
        web_site = web_byte.decode('utf-8')
        soup = BeautifulSoup(web_site, 'html.parser')

        currentPricePerSM = getPricePerSM(soup)
        pricePerSM.extend(currentPricePerSM)
        # print("Ft/m2",pricePerSM,"\n")
        currentTotalPrice = getTotalPrice(soup)
        totalPrice.extend(currentTotalPrice)
        # print("total prices", totalPrice,"\n")
        currentPage = currentPage+1

    # calculate rent 
    #m2+2-2-szoba
    currentPage = 1
    for x in range(maxPages):
        print("currentPage: " + str(currentPage))
        if district == "":
            url ="https://ingatlan.com/szukites/kiado+lakas+" + city + "+20-50-m2+2-2-szoba-alatt?page=" + str(currentPage)
        else: 
            url ="https://ingatlan.com/szukites/kiado+lakas+" + district+ "-ker+20-50-m2+2-2-szoba-alatt?page=" + str(currentPage)

        # print("url generated for renting: " + url)
        req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

        web_byte = urlopen(req, timeout=10).read()
        web_site = web_byte.decode('utf-8')
        soup = BeautifulSoup(web_site, 'html.parser')

        currentRentPrice = getRentPrice(soup)
        rentPrice.extend(currentRentPrice)
        currentPage = currentPage +1

    with open(fileName, "a") as myfile:

        cleanPricePerSM = reject_outliers(pricePerSM)
        formattedCleanPricePerSM= formatPrices(cleanPricePerSM)

        cleanTotalPrice = reject_outliers(totalPrice)
        formattedCleanTotalPrice = formatPrices(cleanTotalPrice)

        cleanRentPrice = reject_outliers(rentPrice)
        formattedCleanRentPrice = formatPrices(cleanRentPrice)
       
        avg = mean(cleanRentPrice)*12 / mean(cleanTotalPrice)

        myfile.write("\n")
        rest = formattedCleanPricePerSM + "," + str(len(cleanTotalPrice)) + "," +formattedCleanTotalPrice + "," + str(len(cleanRentPrice)) +"," + formattedCleanRentPrice + "," + str(round( avg* 100,2 ))
        if district != "":
            myfile.write(city + "," + district + "," + rest)
        else: 
            myfile.write(city + "," + " " + "," + rest  )
print(colored('Hi Attila! This program will do some math for you! \n', 'red')) 
print(colored("it calculates average prices with the following conditions for the flat: \n up to 2 rooms \n 30 - 50 m2 \n", 'blue'))
generateFile()
main()

