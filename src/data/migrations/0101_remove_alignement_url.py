# Generated by Django 4.1.3 on 2022-12-14 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0100_remove_historique_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alignement',
            name='url',
        ),
    ]
