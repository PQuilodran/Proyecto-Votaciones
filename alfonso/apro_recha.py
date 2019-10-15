from pymongo import MongoClient
from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
import requests



sesiones=[]


#####################     SESIONES   ########################


 
html_sesiones = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=51")
respuesta = BeautifulSoup(html_sesiones.read(),"html5lib")
t = respuesta.findAll("id")
for tag in t:
    h=tag.getText()
    sesiones.append(h)


#####################   FIN SESIONES  ######################

for k in range(10):
    lista=[]
    url = 'http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID='+sesiones[k]
    try:
     
        html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+sesiones[k])
     
    except HTTPError as e:
     
        print(e)
     
    except URLError:
     
        print("Server down or incorrect domain")
    else:
        source = requests.get(url)
        content = source.content
        soup = BeautifulSoup(source.content, "html.parser")

        for a in soup.findAll('proyecto_ley'):
            me=a.get("boletin")
            lista.append(me)
           
        res = BeautifulSoup(html.read(),"html5lib")

        print("------------- SESION ID= "+sesiones[k],"  ---------------")
        print("")
        for j in range(len(lista)):
            re=""
            texto=" "
            ress=[]
            aux=lista[j]
            print("para el boletin "+aux+" el resultado fue: ")
            tags = res.find("proyecto_ley", {"boletin": aux})
            
            texto=tags.getText()

            resul = res.findAll("votacion", {"resultado": "APROBADO"})
            for r in resul:
                re=r.getText()
                ress.append(re)
            if len(ress)!= len(lista):
                try:
                    ress[j]
                except IndexError:
                    print('RECHAZADO O EN DISCUCION')
                else:
                    if ress[j]!="":
                        print ('APROBADO')
                    else:
                        print('RECHAZADO')
            else:
                 if len(ress)== len(lista):
                    if ress[j]!="":
                        print ('APROBADO')
                    else:
                        print('RECHAZADO')
        
    print("")

            
connection = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
database = connection['parlamentarios']
collection = database['data']
#datas = {'votacion': '"'+texto+'"'}
#collection.insert_one(datas)
