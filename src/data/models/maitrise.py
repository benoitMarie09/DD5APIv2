from .base import BaseModel
from django.db import models


class Maitrise(BaseModel):
    type = models.ForeignKey('CategorieEquipement',
                             blank=True, null=True, on_delete=models.CASCADE)
    ref_equip = models.ForeignKey(
        'Equipement', blank=True, null=True, on_delete=models.CASCADE)
    ref_comp = models.ForeignKey(
        'Competence', blank=True, null=True, on_delete=models.CASCADE)

