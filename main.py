from fastapi import FastAPI
from pymongo.mongo_client import MongoClient

app = FastAPI()





uri = "mongodb+srv://negaarabolhasani:BOKsFKCrH9J2DDzH@todolist.q5mjj.mongodb.net/?retryWrites=true&w=majority&appName=ToDoList"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# @app.get("/")
# async def root():
#     return {"message": "Wellcome to the app"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
