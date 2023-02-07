# Generated by Django 4.1.3 on 2023-01-03 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0104_alter_niveau_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NiveauClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.IntegerField(default=1)),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.classe')),
            ],
        ),
        migrations.AlterModelOptions(
            name='niveau',
            options={'ordering': ['classe', 'niveau']},
        ),
        migrations.CreateModel(
            name='PJ',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('index', models.CharField(default='default', max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='description')),
                ('alignement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pj', to='data.alignement')),
                ('caracteristiques', models.ManyToManyField(blank=True, related_name='pj', through='data.ValeurCaracteristique', to='data.caracteristique')),
                ('classes', models.ManyToManyField(blank=True, related_name='pj', through='data.NiveauClasse', to='data.classe')),
                ('competences', models.ManyToManyField(blank=True, related_name='pj', to='data.competence')),
                ('equipements', models.ManyToManyField(blank=True, related_name='pj', through='data.QuantiteEquipement', to='data.equipement')),
                ('historique', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pj', to='data.historique')),
                ('langues', models.ManyToManyField(blank=True, related_name='pj', to='data.langue')),
                ('maitrises', models.ManyToManyField(blank=True, related_name='pj', to='data.maitrise')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pj', to='data.sousrace')),
                ('sorts', models.ManyToManyField(blank=True, related_name='pj', to='data.sort')),
            ],
            options={
                'ordering': ['index'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='niveauclasse',
            name='pj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.pj'),
        ),
        migrations.AddField(
            model_name='niveauclasse',
            name='sous_classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.sousclasse'),
        ),
        migrations.AddField(
            model_name='quantiteequipement',
            name='pj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quantite_equipement', to='data.pj'),
        ),
        migrations.AddField(
            model_name='valeurcaracteristique',
            name='pj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='valeur_caract', to='data.pj'),
        ),
    ]