from django import forms
from .models import Enseignant, Materiel, Emprunt, Salle

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['type', 'description', 'salle', 'possesseur', 'proprietaire', 'accessoires', 'date_acquisition']
        widgets = {
            'date_acquisition': forms.DateInput(attrs={'type': 'date'})
        }

class ChangementPossesseurForm(forms.Form):
    nouveau_possesseur = forms.ModelChoiceField(queryset=Enseignant.objects.all())

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
