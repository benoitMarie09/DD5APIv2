# Generated by Django 4.1.3 on 2022-12-06 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_arme_portee_arme_portee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arme',
            old_name='categorie_portee',
            new_name='type',
        ),
    ]