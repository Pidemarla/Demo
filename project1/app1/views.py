from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is my first app")
def demo(request):
    return HttpResponse("This is demo page in app")