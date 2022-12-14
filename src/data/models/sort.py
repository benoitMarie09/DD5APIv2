from django.db import models
from .base import BaseModel


class Sort(BaseModel):
    CHOIX_ATTAQUE = [
        ('cac', 'corps à corps'),
        ('distance', 'distance'),
        (None, 'aucune'),
    ]
    niveaux_superieurs =  composante_desc = models.TextField(
        'description aux niveaux supèrieur', null=True, blank=True)
    niveau = models.IntegerField(default=1)
    ecole = models.ForeignKey(
        'EcoleMagie', blank=True, null=True, related_name='sort', on_delete=models.CASCADE)
    rituel = models.BooleanField(default=False)
    concentration = models.BooleanField(default=False)
    temps_incantation = models.CharField(
        "temps d'incantation", blank=True, default='1 action', max_length=50)
    duree = models.CharField(
        "durée du sort", null=True, blank=True, default=None, max_length=50)
    portee = models.CharField(
        "portée du sort", null=True, blank=True, default=None, max_length=50)
    composantes = models.ManyToManyField('Composante', blank=True)
    composante_desc = models.TextField(
        'composantes description', null=True, blank=True)
    jets_sauvegardes = models.ForeignKey(
        'Caracteristique', null=True, blank=True, related_name='sort', on_delete=models.CASCADE)
    reussite_JdS = models.CharField(
        "réussite JdS", null=True, blank=True, default=None, max_length=50)
    jet_attaque = models.CharField(
        "jets d'attaque", null=True, blank=True, default=None, max_length=50, choices=CHOIX_ATTAQUE)
    degats_par_niveaux = models.ForeignKey('DegatSortNiveaux',null=True, blank=True, on_delete=models.CASCADE)
    degats_par_emplacement = models.ForeignKey('DegatSortEmplacements',null=True, blank=True, on_delete=models.CASCADE)
    soins_par_emplacement = models.ForeignKey('SoinSortEmplacements',null=True, blank=True, on_delete=models.CASCADE)


class EcoleMagie(BaseModel):
    pass


class Composante(BaseModel):
    abreviation = models.CharField(null=True, blank=True, max_length=50)
    materiel = models.ForeignKey(
        'Equipement', blank=True, null=True, on_delete=models.CASCADE)
    consomme = models.BooleanField(default=False)

    def __str__(self):
        materiel = ""
        if self.abreviation == 'M':
            materiel = '-'+str(self.materiel.index)
        return self.abreviation + materiel

