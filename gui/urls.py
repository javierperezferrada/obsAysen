from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home ,name='home'),
    url(r'^panorama/$', views.panorama ,name='panorama'),
    url(r'^sectores/$', views.sectors ,name='sectors'),
    url(r'^ocupaciones/$', views.activities ,name='activities'),
    url(r'^ocupaciones/detalle$', views.detailActivitie ,name='detailActivitie'),
    url(r'^consejo-asesor/$', views.advice ,name='advice'),
    url(r'^equipo/$', views.team ,name='team'),
    url(r'^quienes-somos/$', views.about ,name='about'),
    ]