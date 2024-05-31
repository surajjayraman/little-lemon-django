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

def menu(request):
    content = "<html><head><style>ul {list-style-type: none; margin: 0; padding: 0;} li {display: inline; margin-right: 10px; color: blue;}</style></head><body><h1>Menu</h1><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></body></html>"
    return HttpResponse(content)    
