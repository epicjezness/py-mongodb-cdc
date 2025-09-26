import random
import time

from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/?replicaSet=rs0&directConnection=true"

if __name__ == "__main__":
    client = MongoClient(MONGO_URI)
    db = client.sales
    collection = db.orders

    print("Starting data simulation...")

    try:
        order_id = 1
        while True:
            # 1. Insert a new document
            new_order = {
                "order_id": order_id,
                "product": random.choice(["Laptop", "Mouse", "Keyboard", "Monitor"]),
                "quantity": random.randint(1, 10),
                "status": "pending",
                "created_at": time.time()
            }
            collection.insert_one(new_order)
            print(f"Inserted order {order_id}")
            order_id += 1
            time.sleep(3)

            # 2. Update a previous document (randomly)
            if order_id > 2:
                random_id = random.randint(1, order_id - 1)
                collection.update_one(
                    {"order_id": random_id},
                    {"$set": {"status": "shipped"}}
                )
                print(f"Updated status for order {random_id} to 'shipped'")
                time.sleep(3)

            # 3. Delete a document (randomly)
            if order_id > 5:
                random_id = random.randint(1, order_id - 1)
                collection.delete_one(
                    {"order_id": random_id}
                )
                print(f"Deleted order {random_id}")
                time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")
