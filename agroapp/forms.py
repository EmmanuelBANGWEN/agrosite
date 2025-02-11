from django import forms

# class ContactForm(forms.Form):
#     nom = forms.CharField(max_length=100, label="Votre nom")
#     email = forms.EmailField(label="Votre email")
#     message = forms.CharField(widget=forms.Textarea, label="Votre message")


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Nom")
#     email = forms.EmailField(label="Adresse Email")
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea, label="Message")

from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Adresse Email")
    number = forms.CharField(label="Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")