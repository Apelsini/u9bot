from django.shortcuts import render
from django.http import HttpResponse
import requests, json
import pymongo  #this is for c19cd view
from pymongo import MongoClient
from tabulate import tabulate

EARTH_RADIUS = 6371.0  #c19cd
MDB_URL = "mongodb+srv://readonly:readonly@covid-19.hip2i.mongodb.net/covid19" #c19cd source

def index(request):
    return HttpResponse("Hello, world. You're at the bot index. Checking the change in the message")

def c19(request): # this view gets vaccination rate about Belarus from Our world in data
    url = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json")
    text = url.text
    data = json.loads(text)
    country = data[19] #Belarus is no 19 in the Our World in Data list
    return HttpResponse(json.dumps(country['data']),content_type="application/json")

def c19cd(request):
    client = MongoClient(MDB_URL)
    db = client.get_database("covid19")
    stats = db.get_collection("global_and_us")
    metadata = db.get_collection("metadata")

    # Get some results for the UK:
    print("\nMost recent 10 global_and_us for Belarus:")
    results = (
        stats.find({"country": "Belarus", "state": None})
        .sort("date", pymongo.DESCENDING)
        .limit(10)
    )
    return HttpResponse(results)

# Create your views here.
