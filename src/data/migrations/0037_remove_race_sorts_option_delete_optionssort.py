# Generated by Django 4.1.3 on 2022-12-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0036_optionscompetence_classe_options_competences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='sorts_option',
        ),
        migrations.DeleteModel(
            name='OptionsSort',
        ),
    ]
