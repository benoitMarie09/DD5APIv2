# Generated by Django 4.1.3 on 2022-12-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0065_remove_optionscompetence_parmis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('index', models.CharField(default='default', max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='description')),
                ('nombre_choix', models.IntegerField(default=1, verbose_name='nombre de choix')),
                ('caracteristiques', models.ManyToManyField(blank=True, related_name='caracteristique', to='data.caracteristique')),
                ('competences', models.ManyToManyField(blank=True, related_name='competence', to='data.competence')),
                ('equipements', models.ManyToManyField(blank=True, related_name='equipements', to='data.equipement')),
                ('langues', models.ManyToManyField(blank=True, related_name='langues', to='data.langue')),
                ('maitrises', models.ManyToManyField(blank=True, related_name='maitrise', to='data.maitrise')),
                ('sorts', models.ManyToManyField(blank=True, related_name='sorts', to='data.sort')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
