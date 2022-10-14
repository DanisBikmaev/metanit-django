from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
  
def index(request):
    host = request.META['HTTP_HOST'] # server adres
    user_agent = request.META['HTTP_USER_AGENT'] # browser date
    path = request.path # path
    return HttpResponse(f'''<h2>Main</h2>
                        <p>Host: {host}</p>
                        <p>User-agent: {user_agent}</p>
                        <p>Path: {path}</p>
                        ''')

def about(request, name, age):
    return HttpResponse(f'''<h2>About</h2>
                        <p><b>Name:</b> {name}</p>
                        <p><b>Age:</b> {age}</p>
                        ''')

def contact(request): 
    return HttpResponse('<h2>Contact</h2>')


