import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import os
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
a=[]


html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=51")
res = BeautifulSoup(html.read(),"html5lib")
tags = res.findAll("id")

for tag in tags:
    h=tag.getText()
    a.append(h)
    urlstring ='http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=' + h+ '\n'
    print (urlstring)
    url = urlstring
    source = requests.get(url)
    content = source.content
    soup = BeautifulSoup(source.content, "html.parser")

    for a in soup.findAll('proyecto_ley'):
        boletines=a.get("boletin")
        print (boletines)
        texto=" "
        html = urlopen(urlstring)
        res = BeautifulSoup(html.read(),"html5lib")
        #for i in range(len(boletines)):    
        tags = res.findAll("proyecto_ley", {"boletin": boletines})
        for tag in tags:
            print(tag.getText())
            texto= texto + tag.getText()

            connection = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
            database = connection['parlamentarios']
            collection = database['data']
            data = {'votacion': '"'+texto+'"'}
            collection.insert_one(data)


