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
from sign_in.views import sign_in,auth_user
from Welcome.views import welcome,arcade,action,puzzle,sport,strategy,welcome_game_play
from registration.views import registration,create_user
from Six_ages.views import mainpage,show_game,filter_type,search,top_chart,logout,making_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('signin/',sign_in,name='signin'),
    path('signin/redirect',auth_user,name='signin'),
    path('signup/',registration,name='signup'),
    path('signup/create_user',create_user,name='signup'),
    path('mainpage/',mainpage,name='mainpage'),
    path('arcade/',arcade,name='arcade'),
    path('action/',action,name='action'),
    path('puzzle/',puzzle,name='puzzle'),
    path('sport/',sport,name='sport'),
    path('strategy/',strategy,name='strategy'),
    path('mainpage/show_game/<game_name>.swf', show_game, name='show_game'),
    path('mainpage/search/', search, name='search'),
    path('mainpage/logout/', logout, name='logout'),
    path('mainpage/mycomment/', making_comment, name='logout'),
    path('mainpage/top_chart/<chart_name>', top_chart, name='top_chart'),
    path('mainpage/filter/<filter_name>/', filter_type, name='filter_type'),
    path('game/<game_name>.swf', welcome_game_play, name='welcome_game_play'),
]
