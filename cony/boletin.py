import requests
from bs4 import BeautifulSoup

url = 'http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3731'
source = requests.get(url)
content = source.content
soup = BeautifulSoup(source.content, "html.parser")

# Now I navigate the soup
for a in soup.findAll('proyecto_ley'):
    print (a.get("boletin"))
