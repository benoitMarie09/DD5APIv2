# Generated by Django 4.1.3 on 2022-12-10 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0086_delete_packequipementclasse'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackEquipementClasse',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('index', models.CharField(default='default', max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='description')),
                ('contenu', models.ManyToManyField(blank=True, related_name='Pack', through='data.QuantiteEquipement', to='data.equipement')),
            ],
            options={
                'ordering': ['index'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='quantiteequipement',
            name='pack_equipement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quantite_equipement', to='data.packequipementclasse'),
        ),
    ]
