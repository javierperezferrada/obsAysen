from django.shortcuts import render

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