# Generated by Django 4.1.3 on 2022-12-08 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0040_rename_options_optionslangue_parmis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='optionscaracteristique',
            old_name='nb',
            new_name='nombre_choix',
        ),
        migrations.RenameField(
            model_name='optionscompetence',
            old_name='nb',
            new_name='nombre_choix',
        ),
        migrations.RenameField(
            model_name='optionsequipement',
            old_name='nb',
            new_name='nombre_choix',
        ),
        migrations.RenameField(
            model_name='optionsmaitrise',
            old_name='nb',
            new_name='nombre_choix',
        ),
        migrations.RenameField(
            model_name='optionssort',
            old_name='nb',
            new_name='nombre_choix',
        ),
    ]
