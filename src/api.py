""""Main api file for backend"""
import csv
import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_key")


app = FastAPI()

@app.get("/")
def read_root():
    """"Returns when base api is called"""
    return {"HI"}

@app.get("/lines")
def read_line():
    """"Returns list of lines"""
    with open('../data/lines.csv', encoding="utf-8", newline='') as line_csv:
        csv_read = csv.DictReader(line_csv)
        line_list = list(csv_read)
    return line_list


@app.get("/stations/{line}")
def read_station(line: str,):
    """"Returns stations on line"""
    file = f'../data/{line}.csv'
    file_exists = os.path.isfile(file)
    if file_exists :
        with open(file, encoding="utf-8", newline='') as station_csv:
            csv_read = csv.DictReader(station_csv)
            station_list = list(csv_read)
        return station_list
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/trains/{map_id}")
async def read_train(map_id: str,):
    """"Returns train eta for station"""
    max_results = 6
    api_url = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" \
              f"{api_key}&mapid={map_id}&max={max_results}&outputType=JSON"
    response = requests.get(api_url, timeout=30)
    return response.json()
