# Generated by Django 4.1.3 on 2022-12-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_delete_equipementaventurier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorieequipement',
            name='url',
        ),
    ]
