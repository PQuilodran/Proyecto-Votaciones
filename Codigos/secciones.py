
from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
c=0
a=[]
try:
 
    html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=51")
 
except HTTPError as e:
 
    print(e)
 
except URLError:
 
    print("Server down or incorrect domain")
 
else:
 
    res = BeautifulSoup(html.read(),"html5lib")
 
    tags = res.findAll("id")
 
    for tag in tags:
 
        print(tag.getText())
        h=tag.getText()
  

    for i in range(0,51):
        a.append(h)

print (a)
