
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('produits', views.produits, name='produits'),
    path('services', views.services, name='services'),
    path('formations', views.formations, name='formations'),
    path('financement', views.financement, name='financement'),
    path('redirection_whatsapp1', views.redirection_whatsapp1, name='redirection_whatsapp1'),
    path('redirection_whatsapp2', views.redirection_whatsapp2, name='redirection_whatsapp2'),
    path('redirection_whatsapp3', views.redirection_whatsapp3, name='redirection_whatsapp3'),
    path('redirection_whatsapp4', views.redirection_whatsapp4, name='redirection_whatsapp4'),
    path('redirection_whatsapp5', views.redirection_whatsapp5, name='redirection_whatsapp5'),
    path('redirection_whatsapp6', views.redirection_whatsapp6, name='redirection_whatsapp6'),
    path('contact', views.contact, name='contact'),


]
