"""Six_age URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from sign_in.views import sign_in
from Welcome.views import welcome,arcade,action,puzzle,sport,strategy
from registration.views import register
from Six_ages.views import mainpage,show_game

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('signin/',sign_in,name='signin'),
    path('signup/',register,name='signup'),
    path('mainpage/',mainpage,name='mainpage'),
    path('arcade/',arcade,name='arcade'),
    path('action/',action,name='action'),
    path('puzzle/',puzzle,name='puzzle'),
    path('sport/',sport,name='sport'),
    path('strategy/',strategy,name='strategy'),
    path('mainpage/show_game/<game_name>.swf', show_game, name='show_game'),
]
