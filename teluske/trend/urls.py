from django.contrib import admin
from django.urls import path , include
# from django.conf.urls import url
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home', views.index, name='index'),
    url(r'^$', RedirectView.as_view(url='home'), name="main-view"),
    path('about', views.about, name='service page'),
    path('contact', views.contact, name='service page'),
    path('service', views.service, name='service page'),
    path('project', views.project, name='service page'),
    path('service', views.service, name='service page'),
    path('team', views.team, name='service page'),


    path('male_service', views.male_service, name='Male Service'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)