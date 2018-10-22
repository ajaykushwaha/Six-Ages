import copy
from django.shortcuts import render, redirect
from registration.models import UserDetails, Avatars
from django import template

register = template.Library()


def registration(request):
    all_avatar = Avatars.objects.all()

    avatar_display = []
    for i in range(0, 11):
        temp = []
        j = 0
        for avatar in all_avatar:
            temp_avatar = copy.deepcopy(avatar)
            if i == j:
                temp_avatar.display = True
            else:
                temp_avatar.display = False
            temp.append(temp_avatar)
            j += 1
        avatar_display.append(temp)

    return render(request, 'registration.html', {'all_avatar': avatar_display,'avatars':all_avatar})


def create_user(request):
    uname = request.POST.get('Username', '')
    eml = request.POST.get('Email', '')
    pwd = request.POST.get('Password', '')
    image_name = request.POST.get('Imagename', '')
    image_name = image_name[8:]
    dr1 = UserDetails(Username=uname, Email=eml, Password=pwd, Avatar_image=image_name)
    dr1.save()
    request.session['UserName']=uname
    return redirect("http://127.0.0.1:8000/mainpage/")
