from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Salle(models.Model):
    numero = models.CharField(max_length=10)
    etage = models.IntegerField()

    def __str__(self):
        return f"Salle {self.numero} - Étage {self.etage}"

class Materiel(models.Model):
    TYPE_CHOICES = [
        ('smartphone', 'Smartphone'),
        ('tablette', 'Tablette'),
        ('ecran', 'Écran'),
        ('video_projecteur', 'Vidéo Projecteur'),
        ('pointeur_laser', 'Pointeur Laser')
    ]
    BUDGET_CHOICES = [
        ('annee_courante', "Budget de l'année courante"),
        ('projets', 'Budget projets'),
        ('financements_exceptionnels', 'Budget financements exceptionnels')
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True, related_name='materiels', default=1)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name='materiels_possedes')
    proprietaire = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='proprietaire_materiel', default=1)
    accessoires = models.TextField()
    date_acquisition = models.DateField()
    budget = models.CharField(max_length=30, choices=BUDGET_CHOICES, default='annee_courante')
    etat_accessoires = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.description[:30]}..."

class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, related_name='emprunts')
    emprunteur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='emprunts')
    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    date_retour_reelle = models.DateField(null=True, blank=True)
    lieu_passation = models.CharField(max_length=100, null=True, blank=True)
    occasion_passation = models.CharField(max_length=100, null=True, blank=True)
    objectif_utilisation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.emprunteur} emprunte {self.materiel} du {self.date_emprunt} au {self.date_retour_prevue}"
