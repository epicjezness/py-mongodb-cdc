# MongoDB Change Data Capture (CDC) with Python

Change Data Capture (CDC) is a design pattern used to track and monitor data changes in a database. This project outlines a basic implementation using **Python** and **MongoDB's Change Streams** to react to real-time data modifications.

-----

## Key Concepts

### Change Streams (The CDC Source)

MongoDB Change Streams are the native, official mechanism for performing CDC. They allow applications to receive notifications whenever data is inserted, updated, or deleted on a collection, database, or deployment.

| Operation Type | Description |
| :--- | :--- |
| **insert** | A new document was added. |
| **update** | An existing document was modified. |
| **delete** | A document was permanently removed. |
| **replace** | An entire document was overwritten. |

-----

## Project Files

This project contains two primary scripts to demonstrate CDC:

| File Name | Role | Description |
| :--- | :--- | :--- |
| **`mongodb_cdc.py`** | **The Listener** | Establishes the MongoDB Change Stream connection and listens continuously for data modification events. This script acts as your downstream processor. |
| **`mongodb_test.py`** | **The Simulator** | Performs various write operations (insert, update, delete) against the MongoDB collection to simulate real-world application transactions and generate events for the listener to consume. |

-----

## Requirements

  * **MongoDB Replica Set:** Change Streams require MongoDB to be running as a **replica set** (or sharded cluster). A standalone instance is insufficient.
  * **Python 3.x**
  * **`pymongo`:** The official MongoDB driver for Python.
    ```bash
    pip install pymongo
    ```