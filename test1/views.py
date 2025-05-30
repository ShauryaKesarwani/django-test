from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hi</h1>")

def home(request):
    return HttpResponse("home!")

def ques_page(request, ques_id):
    return HttpResponse("<h3>%d</h3>" % ques_id)

def post_html(request, num):
    return render(request, "reportcard.html", {'num': range(num)})