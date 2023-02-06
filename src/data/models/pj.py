from django.db import models
from .base import BaseModel

class PJ(BaseModel):
    race =  models.ForeignKey(
        'SousRace', blank=True, null=True, related_name='pj', on_delete=models.CASCADE)
    classes = models.ManyToManyField (
        'Classe', blank=True, related_name='pj', through='NiveauClasse')
    equipements = models.ManyToManyField(
        'Equipement', blank=True, related_name='pj', through='QuantiteEquipement')
    historique = models.ForeignKey(
        'Historique', blank=True, null=True, related_name='pj', on_delete=models.CASCADE)
    competences = models.ManyToManyField(
        'Competence', blank=True, related_name='pj')
    maitrises = models.ManyToManyField(
        'Maitrise', blank=True, related_name='pj')
    alignement = models.ForeignKey(
        'Alignement', blank=True, null=True, related_name='pj', on_delete=models.CASCADE)
    langues = models.ManyToManyField(
        'Langue', blank=True, related_name='pj')
    sorts = models.ManyToManyField(
        'Sort', blank=True, related_name='pj')
    caracteristiques = models.ManyToManyField(
        'Caracteristique', blank=True, related_name='pj', through='ValeurCaracteristique')