# Generated by Django 4.1.3 on 2022-12-10 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0078_alter_equipement_categorie_equipement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='categorie_equipement',
            field=models.ForeignKey(default='outil', on_delete=django.db.models.deletion.CASCADE, to='data.categorieequipement'),
        ),
        migrations.AlterField(
            model_name='equipementaventurier',
            name='categorie_equipement_aventurier',
            field=models.ForeignKey(default='instrument', on_delete=django.db.models.deletion.CASCADE, to='data.categorieequipement'),
        ),
    ]
