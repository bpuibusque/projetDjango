# gestion_materiel/forms.py
from django import forms
from .models import Enseignant, Materiel, Emprunt, Salle

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']

class MaterielForm(forms.ModelForm):
    possesseur = forms.ModelChoiceField(
        queryset=Enseignant.objects.all(),
        required=False,
        empty_label="None"
    )
    class Meta:
        model = Materiel
        fields = ['type', 'description', 'salle', 'possesseur', 'proprietaire', 'accessoires', 'date_acquisition', 'budget', 'etat_accessoires']
        widgets = {
            'date_acquisition': forms.DateInput(attrs={'type': 'date'})
        }

class ChangementPossesseurForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['materiel', 'emprunteur', 'date_emprunt', 'date_retour_prevue', 'lieu_passation', 'occasion_passation', 'objectif_utilisation']
        widgets = {
            'date_emprunt': forms.DateInput(attrs={'type': 'date'}),
            'date_retour_prevue': forms.DateInput(attrs={'type': 'date'}),
            'lieu_passation': forms.TextInput(attrs={'placeholder': 'Lieu de la passation'}),
            'occasion_passation': forms.TextInput(attrs={'placeholder': 'Occasion de la passation'}),
            'objectif_utilisation': forms.TextInput(attrs={'placeholder': "Objectif d'utilisation"})
        }

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['materiel', 'emprunteur', 'date_emprunt', 'date_retour_prevue', 'date_retour_reelle']
        widgets = {
            'date_emprunt': forms.DateInput(attrs={'type': 'date'}),
            'date_retour_prevue': forms.DateInput(attrs={'type': 'date'}),
            'date_retour_reelle': forms.DateInput(attrs={'type': 'date'}),
        }


class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['numero', 'etage']
