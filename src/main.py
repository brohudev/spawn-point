from fastapi import FastAPI
from handlers.fullstack import handle_fullstack

app = FastAPI()


@app.get("/fullstack")
def get_fullstack():
    return handle_fullstack()

@app.get("/")
def get_fullstack():
    response = "this page doesnt return anything useful try to go to /fullstack"
    return response