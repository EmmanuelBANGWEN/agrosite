
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('produits', views.produits, name='produits'),
    path('services', views.services, name='services'),

    path('formations', views.formations, name='formations'),
    path('Formation_developpement_durable', views.dev_durable, name='dev_durable'),
    path('Formation_agriculture_durable', views.agri_durable, name='agri_durable'),

    path('financement', views.financement, name='financement'),
    path('financement/Pret', views.pret, name='pret'),
    path('financement/Subventions', views.subventions, name='subventions'),
    path('financement/investisseurs', views.investisseur, name='investisseur'),

    path('redirection_whatsapp1', views.redirection_whatsapp1, name='redirection_whatsapp1'),
    path('redirection_whatsapp2', views.redirection_whatsapp2, name='redirection_whatsapp2'),
    path('redirection_whatsapp3', views.redirection_whatsapp3, name='redirection_whatsapp3'),
    path('redirection_whatsapp4', views.redirection_whatsapp4, name='redirection_whatsapp4'),
    path('redirection_whatsapp5', views.redirection_whatsapp5, name='redirection_whatsapp5'),
    path('redirection_whatsapp6', views.redirection_whatsapp6, name='redirection_whatsapp6'),

    path('contact', views.contact, name='contact'),


]
