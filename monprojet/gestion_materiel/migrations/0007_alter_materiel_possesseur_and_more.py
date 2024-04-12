# Generated by Django 5.0.3 on 2024-04-12 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_materiel', '0006_alter_materiel_possesseur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='possesseur',
            field=models.ForeignKey(default=7, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materiels_possedes', to='gestion_materiel.enseignant'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='proprietaire',
            field=models.ForeignKey(default=6, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proprietaire_materiel', to='gestion_materiel.enseignant'),
        ),
    ]
