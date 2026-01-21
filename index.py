from fastapi import FastAPI
from routes.note import note
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app=FastAPI()

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

conn=MongoClient("MONGODB_URL",serverSelectionTimeoutMS=5000)
app.include_router(note)