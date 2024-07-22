from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'indirizzo email è obbligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Utente(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    idutente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ente_pubblico = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cognome']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Fornitore(AbstractBaseUser):
    idfornitore = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    azienda = models.CharField(max_length=200)
    ente_pubblico = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cognome', 'azienda']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class TipoRichiesta(models.Model):
    idtiporichiesta = models.AutoField(primary_key=True)
    stato_richiesta = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=10)

    def __str__(self):
        return self.acronimo

class TipoServizio(models.Model):
    idtiposervizio = models.AutoField(primary_key=True)
    tipo_servizio = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_servizio

class RichiestaStd(models.Model):
    idrichiestastd = models.AutoField(primary_key=True)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    tipo_richiesta = models.ForeignKey(TipoRichiesta, on_delete=models.CASCADE)
    numero_passeggeri = models.IntegerField()
    numero_giorni = models.IntegerField()
    data_inizio = models.DateField()
    tipo_servizio = models.ForeignKey(TipoServizio, on_delete=models.CASCADE)

class Servizio(models.Model):
    idservizio = models.AutoField(primary_key=True)
    data = models.DateField()
    luogo_partenza = models.CharField(max_length=200)
    destinazione = models.CharField(max_length=200)
    km_percorsi = models.FloatField()
    richiesta_std = models.ForeignKey(RichiestaStd, on_delete=models.CASCADE)
    ora_partenza = models.TimeField()
    ora_arrivo = models.TimeField()

# Questo codice definisce i modelli Django per le tabelle che hai descritto. Alcune note:

# Ho usato AbstractBaseUser e BaseUserManager per creare modelli di utente personalizzati per Utente e Fornitore. 
# Questo ti permette di usare l'email come campo di accesso invece dello username predefinito.

# I campi password sono gestiti automaticamente da Django e verranno crittografati.
# Ho usato AutoField per gli ID primari, che Django gestirà automaticamente.
# Le relazioni tra le tabelle sono gestite usando ForeignKey.

# Per implementare questo nel tuo progetto Django:

# Crea un nuovo progetto Django se non l'hai già fatto.
# Crea una nuova app all'interno del progetto.
# Copia questi modelli nel file models.py della tua app.
# Aggiungi la tua app a INSTALLED_APPS nel file settings.py.
# Esegui python manage.py makemigrations e python manage.py migrate per creare le tabelle nel database.