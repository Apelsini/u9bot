from django.shortcuts import render
from django.http import HttpResponse
import requests, json


def index(request):
    return HttpResponse("Hello, world. You're at the bot index. Checking the change in the message")

def c19(request): # this view gets vaccination rate about Belarus from Our world in data
    url = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json")
    text = url.text
    data = json.loads(text)
    country = data[19] #Belarus is no 19 in the Our World in Data list
    return HttpResponse(json.dumps(country['data']),content_type="application/json")
# Create your views here.
