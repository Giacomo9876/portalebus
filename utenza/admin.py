# # utenza/admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import Utente, Fornitore, TipoRichiesta, TipoServizio, RichiestaStd, Servizio

# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ('email', 'nome', 'cognome', 'ente_pubblico')
#     search_fields = ('email', 'nome', 'cognome')
#     ordering = ('email',)
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Informazioni personali', {'fields': ('nome', 'cognome', 'ente_pubblico')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'nome', 'cognome', 'ente_pubblico', 'password1', 'password2'),
#         }),
#     )

# class UtenteAdmin(CustomUserAdmin):
#     pass

# class FornitoreAdmin(CustomUserAdmin):
#     list_display = ('email', 'nome', 'cognome', 'azienda', 'ente_pubblico')
#     search_fields = ('email', 'nome', 'cognome', 'azienda')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Informazioni personali', {'fields': ('nome', 'cognome', 'azienda', 'ente_pubblico')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'nome', 'cognome', 'azienda', 'ente_pubblico', 'password1', 'password2'),
#         }),
#     )

# admin.site.register(Utente, UtenteAdmin)
# admin.site.register(Fornitore, FornitoreAdmin)
# admin.site.register(TipoRichiesta)
# admin.site.register(TipoServizio)
# admin.site.register(RichiestaStd)
# admin.site.register(Servizio)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utente, Fornitore, TipoRichiesta, TipoServizio, RichiestaStd, Servizio

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nome', 'cognome', 'ente_pubblico')
    search_fields = ('email', 'nome', 'cognome')
    ordering = ('email',)
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
    filter_horizontal = ()
    list_filter = ()

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

class TipoRichiestaAdmin(admin.ModelAdmin):
    list_display = ('idtiporichiesta', 'stato_richiesta', 'acronimo')
    search_fields = ('stato_richiesta', 'acronimo')

class TipoServizioAdmin(admin.ModelAdmin):
    list_display = ('idtiposervizio', 'tipo_servizio')
    search_fields = ('tipo_servizio',)

class RichiestaStdAdmin(admin.ModelAdmin):
    list_display = ('idrichiestastd', 'utente', 'tipo_richiesta', 'numero_passeggeri', 'numero_giorni', 'data_inizio')
    list_filter = ('tipo_richiesta', 'data_inizio')
    search_fields = ('utente__email', 'utente__nome', 'utente__cognome')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "utente":
            kwargs["queryset"] = Utente.objects.filter(is_active=True)
        if db_field.name == "tipo_richiesta":
            kwargs["queryset"] = TipoRichiesta.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ServizioAdmin(admin.ModelAdmin):
    list_display = ('idservizio', 'data', 'luogo_partenza', 'destinazione', 'km_percorsi', 'ora_partenza', 'ora_arrivo')
    list_filter = ('data',)
    search_fields = ('luogo_partenza', 'destinazione')

admin.site.register(Utente, CustomUserAdmin)
admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(TipoRichiesta, TipoRichiestaAdmin)
admin.site.register(TipoServizio, TipoServizioAdmin)
admin.site.register(RichiestaStd, RichiestaStdAdmin)
admin.site.register(Servizio, ServizioAdmin)