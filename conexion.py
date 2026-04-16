import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def conectionBd(nombre_db: str):
    uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_CLUSTER')}/?appName={os.getenv('DB_APP_NAME')}"
    client = MongoClient(uri)
    return client[nombre_db]
