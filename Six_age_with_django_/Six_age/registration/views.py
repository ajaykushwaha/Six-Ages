from django.shortcuts import render
from .models import UserDetails


def register(request):
    dr1 = UserDetails()
    dr1.Username = 'AK619'
    dr1.Email = 'ajay@gmail.com'
    dr1.Password = 'haha'
    dr1.save()
    return render(request, 'registration.html')
