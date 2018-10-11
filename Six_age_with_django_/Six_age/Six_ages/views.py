from django.shortcuts import render
from Six_ages.models import Game

def mainpage(request):
    objects = Game.objects.all()
    return render(request, 'mainpage.html',{"mygame" : objects})