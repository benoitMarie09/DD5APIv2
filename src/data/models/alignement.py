from django.db import models
from .base import BaseModel


class Alignement(BaseModel):
    abreviation = models.CharField(null=True, blank=True, max_length=2)

