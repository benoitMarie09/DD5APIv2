# Generated by Django 4.1.3 on 2022-12-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0030_rename_capacité_vehicule_capacite_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='capacité',
            new_name='capacité',
        ),
    ]
