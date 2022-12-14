from django.db import models
from .base import BaseModel


class Regle(BaseModel):
    pass


class RegleSousSection(BaseModel):
    regle = models.ForeignKey('Regle', blank=True, null=True,
                              related_name='sous_section', on_delete=models.CASCADE)

