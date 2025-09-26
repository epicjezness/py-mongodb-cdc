import json

import pymongo
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/?replicaSet=rs0&directConnection=true"

if __name__ == '__main__':
    client = MongoClient(MONGO_URI)
    db = client.sales
    collection = db.orders

    print("Listening for changes on 'sales.orders'...")

    try:
        with collection.watch() as stream:
            for change in stream:
                print("\n--- Change Detected! ---")
                print(json.dumps(change, indent=2, default=str))
                print("------------------------")

    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred: {e}")
