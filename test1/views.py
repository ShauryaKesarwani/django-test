from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hi</h1>")

def home(request):
    return HttpResponse("home!")