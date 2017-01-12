import urllib.request
import sys


url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbCompositeQuery version="1.0">
    <resultCount>3103</resultCount>
    <queryId>A6712786</queryId>
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
   
    <queryType>org.pdb.query.simple.ChainTypeQuery</queryType>
  
 
    <containsProtein>@PROTEIN</containsProtein>
    <containsDna>@DNA</containsDna>
    <containsRna>@RNA</containsRna>
    <containsHybrid>@H</containsHybrid>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
   
    <queryType>org.pdb.query.simple.ReleaseDateQuery</queryType>

    <database_PDB_rev.date.comparator>between</database_PDB_rev.date.comparator>

    <database_PDB_rev.date.min>@DATE_FROM</database_PDB_rev.date.min>
    <database_PDB_rev.date.max>@DATE_TILL</database_PDB_rev.date.max>

    <database_PDB_rev.mod_type.comparator><![CDATA[<]]></database_PDB_rev.mod_type.comparator>
    <database_PDB_rev.mod_type.value>1</database_PDB_rev.mod_type.value>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>


"""

print ("querying PDB...\n")

z = sys.argv[1]
y = sys.argv[2]
x = sys.argv[3]

print (z,y,x)
req2=queryText.replace("@DATE_FROM",z)
req3=req2.replace("@DATE_TILL",y)
req5=req3
if x=="Protein":

   req5=req3.replace("@PROTEIN","Y")

elif x=="DNA":
   req5=req3.replace("@DNA","Y")

elif x=="RNA":
   req5=req3.replace("@RNA","Y")

elif x=="Hybrid":
   req5=req3.replace("@H","Y")

req5 = req5.encode('UTF-8') 
req4=urllib.request.Request(url, data=req5)
f = urllib.request.urlopen(req4)
result= (f.read().decode('utf-8'))

if result:
   

    print  (result)
    print ("Found number of PDB entries:", result.count('\n'))

else:

    print ("Failed to retrieve results")