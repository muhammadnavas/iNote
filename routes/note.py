from fastapi import APIRouter, FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from models.note import Note
from config.db import conn
from schemas.note import notesEntity, noteEntity
import os
from dotenv import load_dotenv

note=APIRouter()

note.mount("/static", StaticFiles(directory="static"), name="static")
load_dotenv()
import os
MONGODB_URL = os.getenv("MONGODB_URL")
conn = MongoClient(MONGODB_URL,serverSelectionTimeoutMS=5000 )
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append(
            {
            "id": doc["_id"],
            "title": str(doc["title"]),
            "desc": str(doc["desc"]),
            "important":doc["important"]
        })
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDocs": newDocs}
    )
    
@note.post("/")
async def add_note(request:Request):
    form=await request.form()
    formDict=dict(form)
    formDict["important"]=True if formDict.get("important")=="on" else False
    inserted_note = conn.notes.notes.insert_one(dict(formDict))
    return {"Success":True}