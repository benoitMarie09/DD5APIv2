# Generated by Django 4.1.3 on 2022-12-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_remove_sousrace_bonus_caracteristique_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composante',
            name='name',
        ),
        migrations.AddField(
            model_name='composante',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='composante',
            name='nom',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='composante',
            name='index',
            field=models.CharField(default='default', max_length=50, primary_key=True, serialize=False),
        ),
    ]