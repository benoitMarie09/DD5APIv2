# Generated by Django 4.1.3 on 2022-12-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0059_soin_rename_degatsort_degatsortemplacements_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degatsortniveaux',
            old_name='niveau_2',
            new_name='niveau_11',
        ),
        migrations.RenameField(
            model_name='degatsortniveaux',
            old_name='niveau_3',
            new_name='niveau_17',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_1',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_4',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_6',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_7',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_8',
        ),
        migrations.RemoveField(
            model_name='degatsortniveaux',
            name='niveau_9',
        ),
        migrations.AlterField(
            model_name='degatsortniveaux',
            name='niveau_5',
            field=models.ManyToManyField(blank=True, related_name='niveau_1', to='data.degat'),
        ),
    ]
