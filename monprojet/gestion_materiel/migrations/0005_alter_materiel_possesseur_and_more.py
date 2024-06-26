# Generated by Django 5.0.3 on 2024-04-12 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_materiel', '0004_alter_materiel_proprietaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='possesseur',
            field=models.ForeignKey(default='1 - École', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materiels_possedes', to='gestion_materiel.enseignant'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='proprietaire',
            field=models.ForeignKey(default='2 - Réserve', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proprietaire_materiel', to='gestion_materiel.enseignant'),
        ),
    ]
