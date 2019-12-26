from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'horses/index.html')

def game(request):
    return render(request, 'horses/game.html')