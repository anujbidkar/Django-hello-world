from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("Hello guys welcome to django")