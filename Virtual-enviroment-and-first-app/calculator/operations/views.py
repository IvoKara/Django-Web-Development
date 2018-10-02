from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
def add(request, a, b):
    return HttpResponse(json.dumps({"result": int(a) + int(b)}))

def multiply(request, a, b):
    return HttpResponse(json.dumps({"result": int(a) * int(b)}))

def substract(request, a, b):
    return HttpResponse(json.dumps({"result": int(a) - int(b)}))

def division(request, a, b):
    return HttpResponse(json.dumps({"result": int(a) / int(b)}))

def index(request):
    return HttpResponse(json.dumps({"result": 44}))
