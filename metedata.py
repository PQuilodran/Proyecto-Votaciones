from pymongo import MongoClient
from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup

boletines = ["10268-12"]

texto=" "
try:
 
    html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3731")
 
except HTTPError as e:
 
    print(e)
 
except URLError:
 
    print("Server down or incorrect domain")
 
else:

    
    res = BeautifulSoup(html.read(),"html5lib")
    #for i in range(len(boletines)):    
    tags = res.findAll("proyecto_ley", {"boletin": '10268-12'})
    for tag in tags:
        print(tag.getText())
        texto=texto + tag.getText()

connection = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
database = connection['parlamentarios']
collection = database['data']
data = {'votacion': '"'+texto+'"'}
collection.insert_one(data)
