from django.db import models
from .base import BaseModel


class Langue(BaseModel):
    CHOIX_TYPE = [
        ('standard', 'standard'),
        ('exotic', 'exotic')
    ]
    type = models.CharField(null=True, blank=True,
                            choices=CHOIX_TYPE, max_length=10)
    race_typiques = models.ManyToManyField('RaceTypique', blank=True)


class RaceTypique(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nom
