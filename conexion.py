import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def conectionBd(nombre_db: str):
    uri= os.getenv("MONGO_URI")
    client = MongoClient(uri)
    return client[nombre_db]

