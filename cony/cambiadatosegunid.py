import pymongo
from pymongo import MongoClient
from bson import ObjectId

def actualizar(nn, producto):
    con = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = con['parlamentarios']
    # colección
    collection = db['Diccionario']
    resultado = collection.update({'_id': ObjectId(nn)}, {'$set': {"votaciones": producto}})
    return resultado

# conexión
con = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = con['parlamentarios']
# colección
collection = db['Diccionario']
resultado = collection.find({})
for document in resultado:
        nn= (document['_id'])
        print (nn)



print (actualizar(nn ,"dato a cambiar " ))

