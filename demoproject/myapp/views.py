from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.template import loader 

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

def load_template(request):
    template = loader.get_template('myapp/template/index.html') 
    context={}  
    return HttpResponse(template.render(context, request)) 

def url_path(request):
    msg=f""" <br>
    <br>path: {request.path}
    <br>path_info: {request.path_info}
    <br>full_path: {request.get_full_path()}
    <br>is_secure: {request.is_secure()}
    <br> scheme: {request.scheme}
    <br> method: {request.method}
    <br> encoding: {request.encoding}
    <br> User agent: {request.META['HTTP_USER_AGENT']}
    <br> Address: {request.META['REMOTE_ADDR']}
   
    """
    # path = request.path
    return HttpResponse(msg, content_type='text/html', charset='utf-8')
