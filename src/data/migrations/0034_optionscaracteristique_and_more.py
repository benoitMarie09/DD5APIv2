# Generated by Django 4.1.3 on 2022-12-07 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_remove_race_bonus_caracteristique_option_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionsCaracteristique',
            fields=[
                ('type', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True)),
                ('nb', models.IntegerField(default=1, verbose_name='nombre de choix')),
                ('options', models.ManyToManyField(blank=True, related_name='caracteristique', to='data.caracteristique')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='bonus_caracteristique_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='race', to='data.optionscaracteristique'),
        ),
    ]
