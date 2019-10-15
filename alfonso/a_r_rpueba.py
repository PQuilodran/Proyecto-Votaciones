from pymongo import MongoClient
from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup

connection = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
database = connection['parlamentarios']

cproyecto = database['proyectos']
cdata = database['data']

cursor = cproyecto.find()
for fut in cursor:
    print ("%s - %s - %s" \
          %(fut['id'], fut['nombre'], fut['area']))



