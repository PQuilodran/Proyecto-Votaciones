from urllib.request import urlopen
from bs4 import BeautifulSoup
 
a=[]
 
html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=51")
res = BeautifulSoup(html.read(),"html5lib")
tags = res.findAll("id")
for tag in tags:
    h=tag.getText()
    a.append(h)
print (a)
