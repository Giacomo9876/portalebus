# utenza/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UtenteRegistrationForm, FornitoreRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from django.conf import settings

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout effettuato con successo.')
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login effettuato con successo!')
            return redirect('benvenuto')  # Reindirizza alla pagina di benvenuto
        else:
            messages.error(request, 'Email o password non validi.')
    return render(request, 'utenza/login.html')

def home(request):
    return render(request, 'utenza/home.html')

def registrazione_utente(request):
    if request.method == 'POST':
        form = UtenteRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrazione utente effettuata con successo!')
            return redirect('benvenuto')
    else:
        form = UtenteRegistrationForm()
    return render(request, 'utenza/registrazione_utente.html', {'form': form})

def registrazione_fornitore(request):
    if request.method == 'POST':
        form = FornitoreRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrazione fornitore effettuata con successo!')
            return redirect('benvenuto')
    else:
        form = FornitoreRegistrationForm()
    return render(request, 'utenza/registrazione_fornitore.html', {'form': form})



@login_required
def benvenuto(request):
    return render(request, 'utenza/benvenuto.html')

def geocode(address):
    # Usiamo Nominatim per il geocoding (gratuito, ma con limiti di utilizzo)
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    response = requests.get(url)
    data = response.json()
    if data:
        return f"{data[0]['lon']},{data[0]['lat']}"
    return None


# def calcola_percorso(request):
#     if request.method == 'POST':
#         partenza = request.POST.get('partenza')
#         destinazione = request.POST.get('destinazione')
        
#         # Qui dovresti usare un'API come Google Maps o OpenStreetMap
#         # Per questo esempio, useremo un'API gratuita chiamata OpenRouteService
        
#         api_key = '5b3ce3597851110001cf6248dff3049856b5448da45caa5213ec1061'  # Sostituisci con la tua chiave API di OpenRouteService
#         url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={partenza}&end={destinazione}"
        
#         response = requests.get(url)
#         data = response.json()
        
#         if 'features' in data and len(data['features']) > 0:
#             route = data['features'][0]['properties']['segments'][0]
#             distance = route['distance'] / 1000  # Convert to km
#             duration = route['duration'] / 60  # Convert to minutes
            
#             result = {
#                 'distance': f"{distance:.2f} km",
#                 'duration': f"{duration:.0f} minuti",
#             }
#         else:
#             result = {'error': 'Impossibile calcolare il percorso'}
        
#         return JsonResponse(result)
    
#     return JsonResponse({'error': 'Metodo non valido'})

def calcola_percorso(request):
    if request.method == 'POST':
        partenza = request.POST.get('partenza')
        destinazione = request.POST.get('destinazione')
        
        partenza_coord = geocode(partenza)
        destinazione_coord = geocode(destinazione)
        
        if not partenza_coord or not destinazione_coord:
            return JsonResponse({'error': 'Impossibile trovare le coordinate per i luoghi specificati'})
        
        api_key = settings.OPENROUTESERVICE_API_KEY  # Assicurati di aver impostato questa variabile in settings.py
        url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={partenza_coord}&end={destinazione_coord}"
        
        response = requests.get(url)
        data = response.json()
        
        if 'features' in data and len(data['features']) > 0:
            route = data['features'][0]['properties']['segments'][0]
            distance = route['distance'] / 1000  # Convert to km
            duration = route['duration'] / 60  # Convert to minutes
            
            result = {
                'distance': f"{distance:.2f} km",
                'duration': f"{duration:.0f} minuti",
            }
        else:
            result = {'error': 'Impossibile calcolare il percorso'}
        
        return JsonResponse(result)
    
    return JsonResponse({'error': 'Metodo non valido'})
