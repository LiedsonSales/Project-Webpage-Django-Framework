from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('clean page not found message 111')

def second(request):
    return HttpResponse('this is the second page')

def third(request):
    return HttpResponse('this is the third page')