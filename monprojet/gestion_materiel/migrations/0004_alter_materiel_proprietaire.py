# Generated by Django 5.0.3 on 2024-04-12 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_materiel', '0003_alter_materiel_proprietaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='proprietaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proprietaire_materiel', to='gestion_materiel.enseignant'),
        ),
    ]
