from django.urls import path
from .views import ajouter_enseignant, ajouter_materiel, changement_possesseur, home, visualisation, ajouter_emprunt, modifier_emprunt, supprimer_emprunt, modifier_enseignant, supprimer_enseignant, modifier_salle, supprimer_salle, modifier_materiel, supprimer_materiel

urlpatterns = [
    path('ajouter_enseignant/', ajouter_enseignant, name='ajouter_enseignant'),
    path('ajouter_materiel/', ajouter_materiel, name='ajouter_materiel'),
    path('changement_possesseur/<int:pk>/', changement_possesseur, name='changement_possesseur'),
    path('visualisation/', visualisation, name='visualisation'),
    path('ajouter_emprunt/', ajouter_emprunt, name='ajouter_emprunt'),
    path('modifier_emprunt/<int:pk>/', modifier_emprunt, name='modifier_emprunt'),
    path('supprimer_emprunt/<int:pk>/', supprimer_emprunt, name='supprimer_emprunt'),
    path('modifier_enseignant/<int:pk>/', modifier_enseignant, name='modifier_enseignant'),
    path('supprimer_enseignant/<int:pk>/', supprimer_enseignant, name='supprimer_enseignant'),
    path('modifier_salle/<int:pk>/', modifier_salle, name='modifier_salle'),
    path('supprimer_salle/<int:pk>/', supprimer_salle, name='supprimer_salle'),
    path('modifier_materiel/<int:pk>/', modifier_materiel, name='modifier_materiel'),
    path('supprimer_materiel/<int:pk>/', supprimer_materiel, name='supprimer_materiel'),
    path('', home, name='home'),
]
