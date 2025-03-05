from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from .models import Contact
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {name}",
                message=f"De : {name}\nNuméro : {number}\n Email: ({email}\n message venant du formulaire de la page de Contact\n\n Source: site web africangreenfood.com\nMessage: ({message})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

    # return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def produits(request):
    return render(request, 'produits.html')

def services(request):
    return render(request, 'services.html')

def formations(request):
    return render(request, 'formations.html')


def dev_durable(request):
    return render(request, 'developement_durable.html')

def agri_durable(request):
    return render(request, 'agriculture_durable.html')




def financement(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {name}",
                message=f"De : {name}\nNuméro : {number}\n Email: ({email}\nmessage venant du formulaire de la page de financement\n\n source: site web africangreenfood.com\nMessage: ({message})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('financement')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'financement.html', {'form': form})


def pret(request):
    return render(request, 'pret.html')

def subventions(request):
    return render(request, 'subventions.html')

def investisseur(request):
    return render(request, 'investisseur.html')

def redirection_whatsapp1(request):
    return render(request, 'redirect_whatsapp1.html')

def redirection_whatsapp2(request):
    return render(request, 'redirect_whatsapp2.html')

def redirection_whatsapp3(request):
    return render(request, 'redirect_whatsapp3.html')

def redirection_whatsapp4(request):
    return render(request, 'redirect_whatsapp4.html')

def redirection_whatsapp5(request):
    return render(request, 'redirect_whatsapp5.html')

def redirection_whatsapp6(request):
    return render(request, 'redirect_whatsapp6.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {name}",
                message=f"De : {name}\nNuméro : {number}\n Email: ({email}\n message venant du formulaire de la page de Contact\n\n Source: site web africangreenfood.com\nMessage: ({message})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
