from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from handlers.fullstack import handle_fullstack

app = FastAPI()


@app.get("/fullstack", response_class=PlainTextResponse)
def get_fullstack():
    return handle_fullstack()

@app.get("/")
def get_fullstack():
    response = "this page doesnt return anything useful try to go to /fullstack"
    return response