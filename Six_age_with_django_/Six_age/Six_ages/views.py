from django.shortcuts import render
from django.http import HttpResponseNotFound
from Six_ages.models import Game


def mainpage(request):
    objects = Game.objects.all()
    return render(request, 'mainpage.html', {"mygame": objects})


def show_game(request, game_name):
    return render(request, 'show_games.html', {"game_title": game_name})


def filter_type(request, filter_name):
    objects = Game.objects.filter(game_type=filter_name)
    if filter_name == "Arcade":
        return render(request, 'mainpage.html', {"mygame": objects, "active2": 'active'})
    elif filter_name == "Action":
        return render(request, 'mainpage.html', {"mygame": objects, "active3": 'active'})
    elif filter_name == "Puzzle":
        return render(request, 'mainpage.html', {"mygame": objects, "active4": 'active'})
    elif filter_name == "Sport":
        return render(request, 'mainpage.html', {"mygame": objects, "active5": 'active'})
    elif filter_name == "Strategy":
        return render(request, 'mainpage.html', {"mygame": objects, "active6": 'active'})
    else:
        return HttpResponseNotFound("No such category")



