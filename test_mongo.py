
MONGODB_URI = 'mongodb://localhost:27017'
from pymongo import MongoClient


client = MongoClient(MONGODB_URI)
db = client.sol_wallets
wallets_collection = db.wallets

found_docs = list(wallets_collection.find(
        {
           # "address": {"$in": accounts},
           # "status": "active"
        }
    ))
print(found_docs)