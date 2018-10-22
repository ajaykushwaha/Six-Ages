from django.shortcuts import render, redirect
from django.shortcuts import render
from registration.models import UserDetails


def sign_in(request):
    display_error = ""
    try:
        error = request.GET.get('error')
        if int(error) == 1:
            display_error = "Username or the password is incorrect"
    except:

        display_error = ""
    return render(request, 'signIn.html',{'display_error':display_error})


def auth_user(request):
    uname = request.POST.get('Username', '')
    pwd = request.POST.get('Password', '')
    no_objects = UserDetails.objects.filter(Username=uname, Password=pwd).count()
    if no_objects == 1:
        request.session['UserName'] = uname
        return redirect("http://127.0.0.1:8000/mainpage")
    else:
        return redirect("http://127.0.0.1:8000/signin/?error=1")