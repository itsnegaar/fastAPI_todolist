from fastapi import APIRouter
from models.todos import Todo
from schema.schemas import list_serial
from config.database import collection_name
from bson.objectid import ObjectId

router = APIRouter()


#GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


#POST request method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

