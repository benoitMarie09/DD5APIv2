from django.db import models
from .base import BaseModel


class Don(BaseModel):
    prerequis_caracteristique = models.ForeignKey(
        'PrerequisCaracteristique', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_maitrise = models.ForeignKey(
        'PrerequisMaitrise', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_race = models.ForeignKey(
        'PrerequisRace', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_magie = models.ForeignKey(
        'PrerequisMagie', null=True, blank=True, related_name='don', on_delete=models.CASCADE)

