from pymongo import MongoClient

client = MongoClient("mongodb+srv://negaarabolhasani:BOKsFKCrH9J2DDzH@todolist.q5mjj.mongodb.net/?retryWrites=true&w=majority&appName=ToDoList")

db = client.todo_db
collection_name = db['todo_collection']