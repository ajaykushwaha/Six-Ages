from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Six_ages.models import Game
from registration.models import UserDetails

def addGame(request):
    return render(request, 'settings.html')


def gotoApproval(request):
    game_name = request.POST.get('game_name', '')
    game_type = request.POST.get('game_type', '')
    game_rating = request.POST.get('game_rating', '')
    game_image = request.FILES['image_file']
    game_swf = request.FILES['swf_file']
    fs = FileSystemStorage()
    file_image = fs.save(game_image.name, game_image)
    file_swf = fs.save(game_swf.name, game_swf)
    dr1 = Game(game_images=file_image, game_swf=file_swf, game_type=game_type, game_rating=game_rating, comment="",
               game_display_name=game_name)
    dr1.save()
    return redirect("http://127.0.0.1:8000/mainpage/setting/add_a_game/")


def removeGamelist(request):
    objects = Game.objects.all()
    return render(request, 'admin_control .html',{"all_game" : objects})


def removeGame(request,game_name_swf):
    Game.objects.filter(game_swf=game_name_swf).delete()
    return redirect("http://127.0.0.1:8000/mainpage/setting/delete_a_game/")


def change_pass(request):
    return render(request, 'Change_password.html')

def change(request):
    username = request.session['UserName']
    old_pass = request.POST.get('old_password', '')
    new_pass = request.POST.get('new_password', '')
    users = UserDetails.objects.filter(Username=username, Password=old_pass)
    if users.count() == 1:
        for object in users:
            object.Password = new_pass
            object.save()
    return redirect("http://127.0.0.1:8000/mainpage/setting/change_pass/")