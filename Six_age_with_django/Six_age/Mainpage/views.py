from django.shortcuts import render

def Mainpage(request):
	return render(request,'mainpage.html')
