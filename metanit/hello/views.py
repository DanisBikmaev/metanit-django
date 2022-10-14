from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse('Index')

def person(request, id):
    people = ['Tom', 'Bob', 'Sam']
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound('Not Found 404')
def access(reques, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest('Noncorrect data')
    if(age > 17): 
        return HttpResponse('Well done')
    else:
        return HttpResponseNotFound('Blocked')
#3
def first_page(request):
    return HttpResponse('First page')

def second_page(request):
    return HttpResponseRedirect('/first_page')

def third_page(request):
    return HttpResponsePermanentRedirect('/')


# 2 
def product(request, id):
    return HttpResponse(f'Product {id}')

def comment(request, id): 
    return HttpResponse(f'Comment {id}')

def question(request, id):
    return HttpResponse(f'question {id} ')

def new(request):
    return HttpResponse('New')

def top(request):
    return HttpResponse('Top')


# 1
def about(request, name, age):
    return HttpResponse(f'''<h2>About</h2>
                        <p><b>Name:</b> {name}</p>
                        <p><b>Age:</b> {age}</p>
                        ''')
    
def contact(request): 
    host = request.META['HTTP_HOST'] # server adres
    user_agent = request.META['HTTP_USER_AGENT'] # browser date
    path = request.path # path
    return HttpResponse(f'''<h2>Contact</h2>
                        <p>Host: {host}</p>
                        <p>User-agent: {user_agent}</p>
                        <p>Path: {path}</p>
                        <p>Hello, metanit</p>
                        ''', headers={'SecretCode': '42'})

def user(request, name='Undefined', age=0): 
    return HttpResponse(f'''<h3>User</h3>
                        <p>Name: {name}</p>
                        <p>Age: {age}</p>''')
