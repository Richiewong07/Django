from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# HTTP RESPONSE --> ADDS BASIC TEXT TO YOUR WEBSITE
def index(request):
    return HttpResponse('Awesome Job guys! This is the index page, of our polls application')