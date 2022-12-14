from django.db import models
from model_utils.managers import InheritanceManager
from .base import BaseModel

class Race(BaseModel):
    parent_race = models.BooleanField(default=False)
    vitesse = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    taille = models.ForeignKey(
        'Taille', null=True, blank=True, related_name='Race', on_delete=models.CASCADE)
    taille_details = models.TextField(null=True, blank=True)
    age = models.TextField(null=True, blank=True)
    poids = models.TextField(null=True, blank=True)
    bonus_caracteristique = models.ManyToManyField(
        'Caracteristique', blank=True, through='ValeurCaracteristique')
    bonus_caracteristique_option = models.ForeignKey(
        'Option', blank=True, related_name='race_caracteristiques', null=True, on_delete=models.CASCADE)
    maitrises_depart = models.ManyToManyField(
        'Maitrise', blank=True, related_name='race')
    maitrises_option = models.ForeignKey(
        'Option', blank=True, related_name='race_maitrises', null=True, on_delete=models.CASCADE)
    langues = models.ManyToManyField('Langue', blank=True, related_name='race')
    langues_option = models.ForeignKey(
        'Option', blank=True, related_name='race_langues', null=True, on_delete=models.CASCADE)
    langues_desc = models.TextField(null=True, blank=True)
    traits = models.ManyToManyField('Trait', blank=True, related_name='race')
    sorts = models.ManyToManyField('Sort', blank=True, related_name='race')
    sorts_option = models.ForeignKey(
        'Option', blank=True, related_name='race_sorts', null=True, on_delete=models.CASCADE)
    objects = InheritanceManager()


class SousRace(Race):
    race = models.ForeignKey('Race', null=True, blank=True,
                             related_name='sous_race', on_delete=models.CASCADE)


class Taille(BaseModel):
    abreviation = models.CharField(null=True, blank=True, max_length=2)
    def __str__(self):
        return f"{self.nom}({self.abreviation})"


class Trait(BaseModel):
    pass
