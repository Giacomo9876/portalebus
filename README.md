###################### PORTALEBUS ##############################

# Portale Prenotazioni Pullman

Questo progetto è un'applicazione web Django per la gestione di prenotazioni di pullman privati e recensioni dei fornitori.

## Caratteristiche

- Registrazione e autenticazione di utenti e fornitori
- Gestione delle richieste di prenotazione
- Calcolo dei percorsi con integrazione di servizi di mappe
- Interfaccia di amministrazione personalizzata

## Requisiti

- Python 3.8+
- Django 4.2+
- Altre dipendenze elencate in `requirements.txt`

## Installazione

1. Clona il repository:

git clone https://github.com/giacomo9876/portale-prenotazioni-pullman.git
cd portale-prenotazioni-pullman


2. Crea un ambiente virtuale e attivalo:

python -m venv venv
source venv/bin/activate  # Su Windows usa venv\Scripts\activate

3. Installa le dipendenze:

pip install -r requirements.txt (file per il momento non necessario)
- Python 3.8+
- Django 4.2+

4. Applica le migrazioni:

python manage.py migrate

5. Crea un superuser:

python manage.py createsuperuser

6. Avvia il server di sviluppo:

python manage.py runserver

## Struttura del Progetto

- `utenza/`: App principale per la gestione degli utenti e delle prenotazioni
- `models.py`: Definizione dei modelli di dati
- `views.py`: Logica delle viste
- `admin.py`: Configurazione dell'interfaccia di amministrazione
- `forms.py`: Form personalizzati
- `urls.py`: Configurazione degli URL

## Modelli

- `Utente`: Gestisce gli account degli utenti
- `Fornitore`: Gestisce gli account dei fornitori di servizi
- `TipoRichiesta`: Definisce i tipi di richieste di prenotazione
- `TipoServizio`: Definisce i tipi di servizi offerti
- `RichiestaStd`: Gestisce le richieste di prenotazione standard
- `Servizio`: Dettagli dei servizi offerti

## Utilizzo

1. Accedi all'interfaccia di amministrazione su `/admin/` per gestire i dati del sistema.
2. Gli utenti possono registrarsi e accedere al portale per effettuare prenotazioni.
3. I fornitori possono registrarsi e gestire i loro servizi.

## Sviluppi Futuri

- Implementazione e aggiunta delle mappe
- Restituzione di una sorta di ticket
- Creazione e messa in sicurezza dell'intero workflow
- Miglioramento dell'interfaccia utente

## Contribuire

Le pull request sono benvenute. Per modifiche importanti, apri prima un issue per discutere cosa vorresti cambiare.

## Licenza

[MIT](https://choosealicense.com/licenses/mit/)