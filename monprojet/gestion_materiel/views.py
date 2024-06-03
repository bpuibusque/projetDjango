from django.shortcuts import render, get_object_or_404, redirect
from .models import Enseignant, Materiel, Emprunt, Salle
from .forms import EnseignantForm, MaterielForm, ChangementPossesseurForm, EmpruntForm, SalleForm

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = EnseignantForm()
    return render(request, 'ajouter_enseignant.html', {'form': form})

def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = MaterielForm()
    return render(request, 'ajouter_materiel.html', {'form': form})

def changement_possesseur(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        form = ChangementPossesseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = ChangementPossesseurForm(initial={'materiel': materiel})
    return render(request, 'changement_possesseur.html', {'form': form, 'materiel': materiel})

def home(request):
    return render(request, 'home.html')

def visualisation(request):
    enseignants = Enseignant.objects.all()
    salles = Salle.objects.all()
    materiels = Materiel.objects.all()
    emprunts = Emprunt.objects.all()
    context = {
        'enseignants': enseignants,
        'salles': salles,
        'materiels': materiels,
        'emprunts': emprunts,
    }
    return render(request, 'visualisation.html', context)

def ajouter_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save()
            # Mise à jour du possesseur du matériel
            materiel = emprunt.materiel
            materiel.possesseur = emprunt.emprunteur
            materiel.save()
            return redirect('visualisation')
    else:
        form = EmpruntForm()
    return render(request, 'ajouter_emprunt.html', {'form': form})

def modifier_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'modifier_emprunt.html', {'form': form})

def supprimer_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        materiel = emprunt.materiel
        materiel.possesseur = None
        materiel.save()
        
        emprunt.delete()
        return redirect('visualisation')
    return render(request, 'supprimer_emprunt.html', {'emprunt': emprunt})

def modifier_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'modifier_enseignant.html', {'form': form})

def supprimer_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('visualisation')
    return render(request, 'supprimer_enseignant.html', {'enseignant': enseignant})

def modifier_salle(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = SalleForm(instance=salle)
    return render(request, 'modifier_salle.html', {'form': form})

def supprimer_salle(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        salle.delete()
        return redirect('visualisation')
    return render(request, 'supprimer_salle.html', {'salle': salle})

def modifier_materiel(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        form = MaterielForm(request.POST, instance=materiel)
        if form.is_valid():
            form.save()
            return redirect('visualisation')
    else:
        form = MaterielForm(instance=materiel)
    return render(request, 'modifier_materiel.html', {'form': form})

def supprimer_materiel(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        materiel.delete()
        return redirect('visualisation')
    return render(request, 'supprimer_materiel.html', {'materiel': materiel})
