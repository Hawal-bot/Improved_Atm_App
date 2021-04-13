
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# Things to be displayed

def index(request):
    return HttpResponse('Hello, world! This is my first Django app ever. So cool :)')
