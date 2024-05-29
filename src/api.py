import csv

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"HI"}

@app.get("/lines")
def read_root():
    with open('../data/lines.csv', newline='') as lineCSV:
        csv_read = csv.DictReader(lineCSV)
        lineList =[row for row in csv_read]
    return lineList


""" @app.get("/Stations/{line}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} """
