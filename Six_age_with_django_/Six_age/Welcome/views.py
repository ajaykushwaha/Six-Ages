from django.shortcuts import render
from Six_ages.models  import Game


def is_login(request):
    try:
        user = request.session['UserName']
        return 1
    except:
        return 0

def welcome(request):
    return render(request, 'welcome.html',{"active1" : 'active',"is_login":is_login(request)})

def arcade(request):
    objects = Game.objects.filter(game_type='Arcade')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active2" : 'active',"is_login":is_login(request)})

def action(request):
    objects = Game.objects.filter(game_type='Action')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active3" : 'active',"is_login":is_login(request)})

def puzzle(request):
    objects = Game.objects.filter(game_type='Puzzle')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active4" : 'active',"is_login":is_login(request)})

def sport(request):
    objects = Game.objects.filter(game_type='Sport')
    print(objects)
    return render(request, 'type_game_show.html',{"mygame" : objects,"active5" : 'active',"is_login":is_login(request)})

def strategy(request):
    objects = Game.objects.filter(game_type='Strategy')
    return render(request, 'type_game_show.html',{"mygame" : objects,"active6" : 'active',"is_login":is_login(request)})


def welcome_game_play(request, game_name):
    return render(request, 'game_play.html', {"game_title": game_name,"is_login":is_login(request)})