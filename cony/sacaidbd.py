import pymongo
from pymongo import MongoClient

# conexión
con = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = con['parlamentarios']
# colección
collection = db['data']
resultado = collection.find({})
for document in resultado:
        print (document['_id'])

 

