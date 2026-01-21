from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL",)
conn = MongoClient(MONGODB_URL,serverSelectionTimeoutMS=5000)