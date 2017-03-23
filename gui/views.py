from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from gui.forms import NewsForm
from gui.models import News
import socket

ip_host = socket.gethostbyname(socket.gethostname())
if ip_host == '127.0.1.1':
	base = 'http://localhost:8000/media/'
else:
	base = 'http://javierperezferrada.pythonanywhere.com/media/'
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
	news = News.objects.all()[:10]
	return render(request,'news.html',{'news':news})

def newNews(request):
	if request.method == 'GET':
		return render(request,'newNews.html')
	if request.method == 'POST':
		form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gui:news')


def deleteNews(request, pk):
	print 'delete delete'
	print pk 
	new = get_object_or_404(News,pk=pk)
	new.delete()
	return redirect('gui:news')