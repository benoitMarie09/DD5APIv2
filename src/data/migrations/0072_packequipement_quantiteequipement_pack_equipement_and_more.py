# Generated by Django 4.1.3 on 2022-12-09 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0071_delete_packequipement'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackEquipement',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('index', models.CharField(default='default', max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='description')),
                ('poids', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('lettre', models.CharField(blank=True, max_length=50, null=True)),
                ('categorie_equipement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.categorieequipement')),
                ('contenu', models.ManyToManyField(blank=True, related_name='pack', through='data.QuantiteEquipement', to='data.equipement')),
                ('prix_objet', models.ManyToManyField(blank=True, through='data.QuantiteMonaie', to='data.monaie')),
            ],
            options={
                'ordering': ['index'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='quantiteequipement',
            name='pack_equipement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quantite_equipement', to='data.packequipement'),
        ),
        migrations.AddField(
            model_name='quantitemonaie',
            name='pack_equipement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prix', to='data.packequipement'),
        ),
    ]