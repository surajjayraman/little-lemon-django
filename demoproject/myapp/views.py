from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def home(request):
    content = "<html><body><h1>Welcome to Little Lemon</h1></body></html>"
    # return HttpResponse("Hello, world. You're at the myapp home page.")
    return HttpResponse(content)

def display_datetime(request):
    now = datetime.now()
    content = "<html><body><h1>Current date and time: " + str(now) + "</h1></body></html>"
    return HttpResponse(content)
