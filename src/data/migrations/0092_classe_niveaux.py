# Generated by Django 4.1.3 on 2022-12-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0091_remove_classe_url_niveau'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='niveaux',
            field=models.ManyToManyField(blank=True, to='data.niveau'),
        ),
    ]
