import pymongo
from pymongo import MongoClient
from numpy import array
from bson.objectid import ObjectId
from bs4 import BeautifulSoup



# conexión
con = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = con['parlamentarios']
# colección
collection = db['data']
file =open("mongo.txt","w")
for inv in collection.find({},{'votacion': 1}):
        
        nuv=inv
        fun=nuv.get('votacion')
        file.write(fun )
        print (fun)

print ("listo")
file.close()
