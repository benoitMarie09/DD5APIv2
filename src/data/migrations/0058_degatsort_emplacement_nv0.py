# Generated by Django 4.1.3 on 2022-12-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0057_degatsort_sort_degats'),
    ]

    operations = [
        migrations.AddField(
            model_name='degatsort',
            name='emplacement_nv0',
            field=models.ManyToManyField(blank=True, related_name='emplacement_nv0', to='data.degat'),
        ),
    ]