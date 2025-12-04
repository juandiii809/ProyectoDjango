from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("<h1>hola, como estas?</h1>")

def hello(request):
    return HttpResponse("hello, how are you?")

def index(request):
    return HttpResponse("<center><h1>este es el index</h1><center>")

def home(request):
    return HttpResponse("hola :), este es el home o inicio")

def casa(request):
    return HttpResponse("hola esta es la casa")
