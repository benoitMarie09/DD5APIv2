# Generated by Django 4.1.3 on 2022-12-08 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0046_vehicule_capacite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sort',
            name='cible',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='degats',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='duree',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='portee',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='temps_incantation',
        ),
    ]