from django.db import models
from .base import BaseModel, endpoint_case, camel_to_snake
from django.urls import reverse


class Historique(BaseModel):
    maitrises_depart = models.ManyToManyField(
        'Maitrise', blank=True, related_name='historique')
    maitrises_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_maitrises', on_delete=models.CASCADE)
    competences = models.ManyToManyField('competence', blank=True)
    langues_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_langues', on_delete=models.CASCADE)
    equipements_depart = models.ManyToManyField(
        'Equipement', blank=True, related_name='historique', through='QuantiteEquipement')
    equipements_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_equipements', on_delete=models.CASCADE)
    monaie_depart = models.ManyToManyField(
        'Monaie', blank=True, related_name='monaie', through='QuantiteMonaie')
    def get_absolute_url(self):
        return reverse(endpoint_case(camel_to_snake(str(self.__class__.__name__))), kwargs={'pk': self.pk})


class Personalite(models.Model):
    historique = models.OneToOneField(
        'Historique', null=True, related_name='personalite', on_delete=models.CASCADE)
    domaine = models.ManyToManyField(
        'DomaineHistorique', blank=True, related_name='personalite')
    capacite = models.ManyToManyField(
        'CapaciteHistorique', blank=True, related_name='personalite')
    trait = models.ManyToManyField(
        'TraitHistorique', blank=True, related_name='personalite')
    ideal = models.ManyToManyField(
        'IdealHistorique', blank=True, related_name='personalite')
    lien = models.ManyToManyField(
        'LienHistorique', blank=True, related_name='personalite')
    Defaut = models.ManyToManyField(
        'DefautHistorique', blank=True, related_name='personalite')

    def __str__(self):
        return f"personalité {self.historique}"


class DefautHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class LienHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class IdealHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class DomaineHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class TraitHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class CapaciteHistorique(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.nom
