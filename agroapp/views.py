from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def produits(request):
    return render(request, 'produits.html')

def services(request):
    return render(request, 'services.html')

def formations(request):
    return render(request, 'formations.html')





def financement(request):
    return render(request, 'financement.html')


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
                message=f"De : {name} ({email})\nNuméro : {number}\n\n{message}",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('financement')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'financement.html', {'form': form})














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



# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Traitement des données du formulaire (par exemple, envoi d'un email)
#             nom = form.cleaned_data['nom']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             # Envoie l'email ou enregistre les données selon ton besoin
#             # Exemple d'envoi d'email (fais attention à configurer ton serveur d'email)
#             # send_mail('Nouveau message de contact', message, email, ['destinataire@example.com'])
#             return render(request, 'merci.html')  # Redirection vers une page de remerciement
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form})



# def contact(request):
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Récupération des données
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             number = form.cleaned_data['number']
#             message = form.cleaned_data['message']

#             # Enregistrement en base de données
#             Contact.objects.create(
#                 name=name,
#                 email=email,
#                 number=number,
#                 message=message
#             )

#             # Envoi de l'email
#             send_mail(
#                 subject=f"Nouveau message de {name}",
#                 message=f"De : {name} ({email})\nNuméro : {number}\n\n{message}",
#                 from_email=email,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#                 fail_silently=False,
#             )

#             messages.success(request, "Votre message a été envoyé avec succès !")
#             return render(request, 'merci.html')  # Redirection vers une page de remerciement
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                    
                # Logique pour envoyer un email (ou sauvegarder dans la base de données)
                send_mail(
                    subject=f"Message de : {name}",
                    message=f"Subject: {subject}\n\nMessage: {message}",
                    from_email=email,
                    recipient_list=['bikoyemmanuel531@gmail.com'],  # Remplacez par l'email de réception
                    )
                
                messages.success(request, 'Votre message a été envoyé avec succès!')
                return redirect('contact')  # Redirection après succès
    
        else:

            messages.error(request, "Vous devez être connecté pour nous contacter.")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})  # Retour au formulaire si GET
