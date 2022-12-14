from django.db import models
from .base import BaseModel


class Etat(BaseModel):
    pass


class Epuisement(Etat):
    niveau = models.IntegerField(default=1)
    effet = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return f"épuisement(nv{self.niveau})"


