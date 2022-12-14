from django.db import models
from .base import BaseModel


class Option(BaseModel):
    nombre_choix = models.IntegerField('nombre de choix', default=1)
    caracteristiques = models.ManyToManyField('caracteristique',related_name='caracteristique', blank=True)
    competences = models.ManyToManyField('Competence',related_name='competence', blank=True)
    maitrises = models.ManyToManyField('Maitrise',related_name='maitrise', blank=True)
    langues = models.ManyToManyField('Langue',related_name='langues', blank=True)
    equipements = models.ManyToManyField('Equipement',related_name='equipements', blank=True)
    categories_equipements = models.ManyToManyField('CategorieEquipement',related_name='categories_equipements', blank=True)
    packs_equipements = models.ManyToManyField('PackEquipementClasse',related_name='categories_equipements', blank=True)
    sorts = models.ManyToManyField('Sort',related_name='sorts', blank=True)
    def __str__(self):
        return f"{self.index}_{self.nombre_choix}_choix"
