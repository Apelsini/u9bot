from django.shortcuts import render
from django.http import HttpResponse


def bot(request):
    return HttpResponse("Hello, world. You're at the bot index. Checking the change in the message")

def c19(request):
    return HttpResponse("covid19 json will be here")
# Create your views here.
