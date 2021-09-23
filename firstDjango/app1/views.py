from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return  HttpResponse('HelloWord!')


# Create your views here.
