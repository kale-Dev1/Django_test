from operator import index
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def list(response,name):
    Is = ToDoList.objects.get(name=name)
    item = Is.item_set.get(id=1)
    return HttpResponse('<h1>%s</><p>%s</>' %(Is.name, str(item.text)))

def kale(response):
    return HttpResponse('<h1>Welcome to my Page. My name is Kale</h1>')

def index(response):
    return HttpResponse('Welcome to my page')