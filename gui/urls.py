from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.home ,name='home'),
    url(r'^panorama-regional/$', views.panorama ,name='panorama'),
    url(r'^panorama/nuevo-reporte$', views.newReport ,name='newReport'),
    url(r'^panorama/eliminar-reporte/(?P<pk>\d+)/$', views.deleteReport ,name='deleteReport'),
    url(r'^sectores/$', views.sectors ,name='sectors'),
    url(r'^sectores/(?P<pk>\d+)/$', views.detailSector ,name='detailSector'),
    url(r'^ocupaciones/$', views.activities ,name='activities'),
    url(r'^ocupaciones/(?P<pk>\d+)/$', views.detailActivitie ,name='detailActivitie'),
    url(r'^consejo-asesor/$', views.advice ,name='advice'),
    url(r'^comite-tecnico/$', views.technicalCommitte ,name='technicalCommitte'),
    url(r'^equipo/$', views.team ,name='team'),
    url(r'^preguntas-frecuentes/$', views.frecuentQuestions ,name='frecuentQuestions'),
    url(r'^quienes-somos/$', views.about ,name='about'),
    url(r'^noticias/$', views.news ,name='news'),
    url(r'^noticias/(?P<pk>\d+)$', views.detailNew ,name='detailNew'),
    url(r'^noticias/pagina/(?P<page>\d+)/$', views.pageNews ,name='pageNews'),
    url(r'^noticias/nueva$', views.newNews ,name='newNews'),
    url(r'^noticias/eliminar/(?P<pk>\d+)/$', views.deleteNews ,name='deleteNews'),
    url(r'^noticias/editar/(?P<pk>\d+)/$', views.updateNews ,name='updateNews'),
    url(r'^ingresar/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^salir/$', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
    url(r'^descargas/$', views.downloads, name='downloads'),
    ]