# Generated by Django 4.1.3 on 2022-12-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0089_remove_classe_equipements_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='equipements_options',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classe_equipements', to='data.option'),
        ),
        migrations.AddField(
            model_name='option',
            name='pack_equipement',
            field=models.ManyToManyField(blank=True, related_name='categories_equipements', to='data.packequipementclasse'),
        ),
    ]