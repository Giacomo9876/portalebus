# utenza/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utente, Fornitore

class UtenteRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Utente
        fields = ('nome', 'cognome', 'email', 'ente_pubblico', 'password1', 'password2')

class FornitoreRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Fornitore
        fields = ('nome', 'cognome', 'azienda', 'email', 'ente_pubblico', 'password1', 'password2')