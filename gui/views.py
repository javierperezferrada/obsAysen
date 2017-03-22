from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def home(request):
	return render(request,'home.html')

def panorama(request):
	return render(request,'panorama.html')

def sectors(request):
	return render(request,'sectors.html')

def activities(request):
	return render(request,'activities.html')

def detailActivitie(request):
	return render(request,'detailActivitie.html')

def advice(request):
	return render(request,'advice.html')

def team(request):
	return render(request,'team.html')

def about(request):
	return render(request,'about.html')

#@login_required(login_url='/login/')
def news(request):
	return render(request,'news.html')