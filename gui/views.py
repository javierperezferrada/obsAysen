from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from gui.forms import NewsForm
from gui.models import News
import math

paginationSize = 20
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
	news = News.objects.all()[:paginationSize]
	total = News.objects.count()
	print total
	totalPages = math.ceil(total/float(paginationSize))
	pages = []
	for p in range(int(totalPages)):
		print p
		if p+1 == 1:
			pages.append({'p':p+1,'class':'active'})
		else:
			pages.append({'p':p+1,'class':''})
	return render(request,'news.html',{'news':news,'pages':pages})

def pageNews(request,page):
	page = int(page)
	newsFrom = (page-1)*paginationSize
	newsTo = page*paginationSize
	news = News.objects.all()[newsFrom:newsTo]
	total = News.objects.count()
	print total
	totalPages = math.ceil(total/float(paginationSize))
	pages = []
	for p in range(int(totalPages)):
		print p
		if p+1 == page:
			pages.append({'p':p+1,'class':'active'})
		else:
			pages.append({'p':p+1,'class':''})
	return render(request,'news.html',{'news':news,'pages':pages})

def newNews(request):
	if request.method == 'GET':
		return render(request,'newNews.html')
	if request.method == 'POST':
		form = NewsForm(request.POST, request.FILES)
		print request.POST
        if form.is_valid():
            form.save()
            return redirect('gui:news')

def updateNews(request, pk, template_name='newNews.html'):
    new = get_object_or_404(News, pk=pk)
    print request.POST
    form = NewsForm(request.POST or None, request.FILES or None,instance=new)
    if form.is_valid():
        form.save()
        return redirect('gui:news')
    return render(request, template_name, {'form':form})

def deleteNews(request, pk,
	template_name='confirm_delete.html'):
	#this function is to delete a news
	new = get_object_or_404(News,pk=pk)
	if request.method=='POST':
		new.delete()
		return redirect('gui:news')
	return render(request, template_name,{'object':new})