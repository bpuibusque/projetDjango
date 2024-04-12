from django.contrib import admin
from .models import Enseignant, Salle, Materiel, Emprunt

class MaterielAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'salle', 'proprietaire', 'possesseur')
    list_filter = ('type', 'salle', 'proprietaire')
    search_fields = ('description',)

class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('materiel', 'emprunteur', 'date_emprunt', 'date_retour_prevue', 'date_retour_reelle')
    list_filter = ('date_emprunt', 'date_retour_prevue')
    search_fields = ('materiel__description', 'emprunteur__nom')

admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Materiel, MaterielAdmin)
admin.site.register(Emprunt, EmpruntAdmin)