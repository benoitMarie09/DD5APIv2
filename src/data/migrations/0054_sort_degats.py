# Generated by Django 4.1.3 on 2022-12-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0053_degatsort'),
    ]

    operations = [
        migrations.AddField(
            model_name='sort',
            name='degats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.degatsort'),
        ),
    ]
