# Generated by Django 4.1.3 on 2022-12-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_remove_categorieequipement_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Instrument',
        ),
        migrations.DeleteModel(
            name='Kit',
        ),
        migrations.DeleteModel(
            name='Outil',
        ),
    ]
