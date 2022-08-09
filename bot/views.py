from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bot index. Checking the change in the message")

# Create your views here.
