from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"HI"}

@app.get("/lines")
def read_root():
    return {"Red Line": "Red"}, {"Blue Line": "Blue"}, {"Brown Line": "Brn"}


""" @app.get("/Stations/{line}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} """
