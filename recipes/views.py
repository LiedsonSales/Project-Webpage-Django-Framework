from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'Liedson'
    })

def sobre(request):
    return render(request, 'recipes/sobre.html')

def contato(request):
    return HttpResponse('this is the third page')