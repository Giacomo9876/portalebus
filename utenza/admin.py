# utenza/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Utente, Fornitore, TipoRichiesta, TipoServizio, RichiestaStd, Servizio

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'nome', 'cognome', 'ente_pubblico')
    search_fields = ('email', 'nome', 'cognome')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informazioni personali', {'fields': ('nome', 'cognome', 'ente_pubblico')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'cognome', 'ente_pubblico', 'password1', 'password2'),
        }),
    )

class UtenteAdmin(CustomUserAdmin):
    pass

class FornitoreAdmin(CustomUserAdmin):
    list_display = ('email', 'nome', 'cognome', 'azienda', 'ente_pubblico')
    search_fields = ('email', 'nome', 'cognome', 'azienda')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informazioni personali', {'fields': ('nome', 'cognome', 'azienda', 'ente_pubblico')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'cognome', 'azienda', 'ente_pubblico', 'password1', 'password2'),
        }),
    )

admin.site.register(Utente, UtenteAdmin)
admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(TipoRichiesta)
admin.site.register(TipoServizio)
admin.site.register(RichiestaStd)
admin.site.register(Servizio)