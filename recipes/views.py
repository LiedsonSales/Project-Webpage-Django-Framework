from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return HttpResponse('this is the second page')

def contato(request):
    return HttpResponse('this is the third page')