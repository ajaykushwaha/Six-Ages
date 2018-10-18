from django.shortcuts import render
from Six_ages.models  import Game

def welcome(request):
    return render(request, 'welcome.html',{"active1" : 'active'})

def arcade(request):
    objects = Game.objects.filter(game_type='Arcade')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active2" : 'active'})

def action(request):
    objects = Game.objects.filter(game_type='Action')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active3" : 'active'})

def puzzle(request):
    objects = Game.objects.filter(game_type='Puzzle')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active4" : 'active'})

def sport(request):
    objects = Game.objects.filter(game_type='Sport')
    print(objects)
    return render(request, 'type_game_show.html',{"mygame" : objects,"active5" : 'active'})

def strategy(request):
    objects = Game.objects.filter(game_type='Strategy')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active6" : 'active'})


def welcome_game_play(request, game_name):
    return render(request, 'game_play.html', {"game_title": game_name})