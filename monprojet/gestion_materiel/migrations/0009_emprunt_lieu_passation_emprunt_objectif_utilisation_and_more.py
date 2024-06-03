# Generated by Django 5.0.3 on 2024-06-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_materiel', '0008_alter_materiel_salle'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='lieu_passation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='objectif_utilisation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='occasion_passation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='materiel',
            name='budget',
            field=models.CharField(choices=[('annee_courante', "Budget de l'année courante"), ('projets', 'Budget projets'), ('financements_exceptionnels', 'Budget financements exceptionnels')], default='annee_courante', max_length=30),
        ),
        migrations.AddField(
            model_name='materiel',
            name='etat_accessoires',
            field=models.TextField(default='neuf'),
        ),
    ]
