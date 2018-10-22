from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound,HttpResponse
from django.core.paginator import Paginator
from registration.models import UserDetails
from Six_ages.models import Game,Comments
from django.http import JsonResponse


def mainpage(request):
    objects = Game.objects.all()
    paginator = Paginator(objects, 24)
    page = request.GET.get('page')
    objects = paginator.get_page(page)

    try:
        uname = request.session['UserName']
        user_images = UserDetails.objects.filter(Username=uname)
        myimage = ""
        for images in user_images:
            myimage = images.Avatar_image
        return render(request, 'mainpage.html', {"mygame": objects, "username": uname,"avatar_image":myimage})
    except:
        return redirect("http://127.0.0.1:8000/")

def show_game(request, game_name):
    try:
        uname = request.session['UserName']
        user_images = UserDetails.objects.filter(Username=uname)
        myimage = ""
        for images in user_images:
            myimage = images.Avatar_image
        return render(request, 'show_games.html', {"game_title": game_name,'username':uname,'avatar_image':myimage})
    except:
        return redirect("http://127.0.0.1:8000/")


def filter_type(request, filter_name):
    objects = Game.objects.filter(game_type=filter_name)
    paginator = Paginator(objects, 24)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    try:
        uname = request.session['UserName']
        user_images = UserDetails.objects.filter(Username=uname)
        myimage = ""
        for images in user_images:
            myimage = images.Avatar_image
        if filter_name == "Arcade":
            return render(request, 'mainpage.html',
                          {"mygame": objects, "active2": 'active', "username": uname,'avatar_image':myimage})
        elif filter_name == "Action":
            return render(request, 'mainpage.html',
                          {"mygame": objects, "active3": 'active', "username": uname,'avatar_image':myimage})
        elif filter_name == "Puzzle":
            return render(request, 'mainpage.html',
                          {"mygame": objects, "active4": 'active', "username": uname,'avatar_image':myimage})
        elif filter_name == "Sport":
            return render(request, 'mainpage.html',
                          {"mygame": objects, "active5": 'active', "username": uname,'avatar_image':myimage})
        elif filter_name == "Strategy":
            return render(request, 'mainpage.html',
                          {"mygame": objects, "active6": 'active', "username": uname,'avatar_image':myimage})
        else:
            return HttpResponseNotFound("No such category")
    except:
        return redirect("http://127.0.0.1:8000/")


def search(request):
    game_name_contains = request.GET.get('term')
    objects = Game.objects.filter(game_display_name__icontains=game_name_contains)
    try:
        uname = request.session['UserName']
        user_images = UserDetails.objects.filter(Username=uname)
        myimage = ""
        for images in user_images:
            myimage = images.Avatar_image
        return render(request, 'mainpage.html',{"mygame": objects, "search_term": game_name_contains, "username": uname,'avatar_image':myimage})

    except:
        return redirect("http://127.0.0.1:8000/")


def top_chart(request,chart_name):
    try:
        uname = request.session['UserName']
        user_images = UserDetails.objects.filter(Username=uname)
        myimage = ""
        for images in user_images:
            myimage = images.Avatar_image
        if chart_name == "t_10_arcade":
            objects = Game.objects.filter(game_type="Arcade").order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "t_10_action":
            objects = Game.objects.filter(game_type="Action").order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "t_10_puzzle":
            objects = Game.objects.filter(game_type="Puzzle").order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "t_10_sport":
            objects = Game.objects.filter(game_type="Sport").order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "t_10_strategy":
            objects = Game.objects.filter(game_type="Strategy").order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "t_10_editors_choice":
            objects = Game.objects.filter().order_by('-game_rating')[:10]
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        elif chart_name == "all_games":
            objects = Game.objects.all()
            paginator = Paginator(objects, 24)
            page = request.GET.get('page')
            objects = paginator.get_page(page)
            return render(request, 'mainpage.html', {"mygame": objects, "username": uname,'avatar_image':myimage})

        else:
            return HttpResponseNotFound("No such category")

    except:
        return redirect("http://127.0.0.1:8000/")


def making_comment(request):
    comment = request.POST.get('comment', '')
    game_name = request.POST.get('game_name', '')
    user_name = request.POST.get('user_name', '')
    dr1 = Comments(comment=comment, game_name=game_name, uname=user_name)
    dr1.save()
    return JsonResponse({'success': 'added the comment'})


def logout(request):
    try:
        del request.session['UserName']
        return redirect("http://127.0.0.1:8000/")
    except KeyError:
        pass
    return HttpResponse("You're logged out.")