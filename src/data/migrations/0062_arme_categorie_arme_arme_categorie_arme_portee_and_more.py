# Generated by Django 4.1.3 on 2022-12-09 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0061_alter_degat_options_remove_arme_categorie_arme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arme',
            name='categorie_arme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie_arme', to='data.categorieequipement'),
        ),
        migrations.AddField(
            model_name='arme',
            name='categorie_arme_portee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie_arme_portee', to='data.categorieequipement'),
        ),
        migrations.AddField(
            model_name='arme',
            name='categorie_portee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie_portee', to='data.categorieequipement'),
        ),
    ]
