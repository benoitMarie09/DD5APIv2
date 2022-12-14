from django.db import models
from .base import BaseModel


class Competence(BaseModel):
    caracteristique = models.ForeignKey(
        'Caracteristique', blank=True, null=True, related_name='competences', on_delete=models.CASCADE)
