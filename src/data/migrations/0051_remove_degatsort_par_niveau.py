# Generated by Django 4.1.3 on 2022-12-08 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0050_remove_degatsort_jds_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degatsort',
            name='par_niveau',
        ),
    ]
