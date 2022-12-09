# Generated by Django 4.1.3 on 2022-12-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0060_rename_niveau_2_degatsortniveaux_niveau_11_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degat',
            options={'ordering': ['type']},
        ),
        migrations.RemoveField(
            model_name='arme',
            name='categorie_arme',
        ),
        migrations.RemoveField(
            model_name='arme',
            name='type',
        ),
        migrations.RemoveField(
            model_name='arme',
            name='type_portee',
        ),
        migrations.AlterField(
            model_name='sort',
            name='temps_incantation',
            field=models.CharField(blank=True, default='1 action', max_length=50, verbose_name="temps d'incantation"),
        ),
    ]
