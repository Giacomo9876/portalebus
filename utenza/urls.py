# utenza/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('registrazione/utente/', views.registrazione_utente, name='registrazione_utente'),
    path('registrazione/fornitore/', views.registrazione_fornitore, name='registrazione_fornitore'),
    path('logout/', views.user_logout, name='logout'),
    path('benvenuto/', views.benvenuto, name='benvenuto'),
    path('calcola-percorso/', views.calcola_percorso, name='calcola_percorso'),
]

# Assicurati di includere queste URL nel file urls.py principale del tuo progetto.

# Questo set up ti fornisce:

# - Integrazione dei modelli nell'interfaccia di amministrazione di Django.
# - Viste semplici per la registrazione di utenti e fornitori.
# - Form personalizzati per la registrazione.
# - Template HTML di base per le pagine di registrazione.

# Per utilizzare queste viste, dovrai:

# - Creare un template di base (base.html) se non l'hai già fatto.
# - Configurare correttamente le impostazioni dei template in settings.py.
# - Gestire l'autenticazione e l'autorizzazione nelle tue viste.
# - Personalizzare ulteriormente i template in base alle tue esigenze di design.