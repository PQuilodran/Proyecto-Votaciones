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
    



