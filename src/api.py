import csv
import requests
import key

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"HI"}

@app.get("/lines")
def read_root():
    with open('../data/lines.csv', newline='') as line_csv:
        csv_read = csv.DictReader(line_csv)
        line_list =[row for row in csv_read]
    return line_list


@app.get("/Stations/{line}")
def read_item(line: str,):
    with open(f"../data/{line}.csv" , newline='') as station_csv:
        csv_read = csv.DictReader(station_csv)
        station_List =[row for row in csv_read]
    return station_List

@app.get("/Trains/{map_id}")
async def read_item(map_id: str,):
    api_key = key.key
    max_results = 6
    api_url = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" \
              f"{api_key}&mapid={map_id}&max={max_results}&outputType=JSON"
    response = requests.get(api_url, timeout=30)
    return response.json()
