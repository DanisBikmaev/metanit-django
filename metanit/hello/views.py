from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
  
def index(request):
    return HttpResponse('<h2>Main</h2>')

def about(request):
    return HttpResponse('<h2>About</h2>')

def contact(request): 
    return HttpResponse('<h2>Contact</h2>')


