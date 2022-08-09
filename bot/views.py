from django.shortcuts import render
from django.http import HttpResponse
import requests, json


def index(request):
    return HttpResponse("Hello, world. You're at the bot index. Checking the change in the message")

def c19(request):
    url = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json")
    text = url.text
    data = json.loads(text)
    country = data[17]
    return HttpResponse(country)
# Create your views here.
