
import urllib.request
import sys
import re
url2='http://www.rcsb.org/pdb/rest/describeMol?structureId=@'
z = sys.argv[1]
req=url2.replace("@",z)
f = urllib.request.urlopen(req)
for l in urllib.request.urlopen(req):
    l= (l.decode('utf-8'))
    start = '<polymerDescription description=\"'
    end = '\"'
    if (re.search(re.escape(start)+"(.*)"+re.escape(end),l)):
      print (l[l.rfind(start)+len(start):l.rfind(end)])

