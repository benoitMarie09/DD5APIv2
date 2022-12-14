from django.db import models
from .base import BaseModel


class Monstre(BaseModel):
    taille = models.ForeignKey(
        'Taille', blank=True, null=True, related_name='Monstre', on_delete=models.CASCADE)
    type = models.CharField(null=True, blank=True, max_length=50)
    alignement = models.ForeignKey(
        'Alignement', blank=True, null=True, related_name='Monstre', on_delete=models.CASCADE)
    classe_armure = models.IntegerField(null=True, blank=True)
    pv = models.IntegerField(null=True, blank=True)
    de_pv = models.CharField(null=True, blank=True, max_length=50)
    vitesse = models.ForeignKey(
        'Vitesse', blank=True, null=True, related_name='Monstre', on_delete=models.CASCADE)
    valeur_caracteristique = models.ManyToManyField(
        'Caracteristique', blank=True, through='ValeurCaracteristique', related_name='valeur_monstre')
    JdS = models.ManyToManyField(
        'JetDeSauvegarde', blank=True, related_name='JdS_monstre')
    competences = models.ManyToManyField(
        'Competence', blank=True, related_name='monstre')
    sens = models.ManyToManyField(
        'SensMonstre', blank=True, related_name='monstre')
    langue = models.ManyToManyField(
        'Langue', blank=True, related_name='monstre')
    capacite_monstre = models.ManyToManyField(
        'CapaciteMonstre', blank=True, related_name='monstre')
    actions = models.ManyToManyField(
        'ActionMonstre', blank=True, related_name='monstre')
    puissance = models.DecimalField(
        decimal_places=2, max_digits=4, null=True, blank=True)
    xp = models.IntegerField(null=True, blank=True)
    immunites_degats = models.ManyToManyField(
        'TypeDegat', blank=True, related_name='immunite_monstre')
    resistance_degats = models.ManyToManyField(
        'TypeDegat', blank=True, related_name='resistance_monstre')
    immunites_etats = models.ManyToManyField('Etat', blank=True)
    bonus_maitrise = models.IntegerField(null=True, blank=True)


class CapaciteMonstre(BaseModel):
    pass


class ActionMonstre(BaseModel):
    nom = models.CharField(null=True, blank=True, max_length=50)
    type = models.CharField(null=True, blank=True, max_length=50)
    bonus_attaque = models.IntegerField(null=True, blank=True)
    degat = models.ManyToManyField(
        'Degat', blank=True, related_name='action_monstre')
    portee = models.ForeignKey(
        'Portee', blank=True, null=True, on_delete=models.CASCADE)
    cible = models.ForeignKey('Cible', null=True, blank=True,
                              related_name='action_monstre', on_delete=models.CASCADE)
    jets_sauvegardes = models.ForeignKey(
        'Caracteristique', null=True, blank=True, related_name='action_monstre', on_delete=models.CASCADE)
    legendaire = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class SensMonstre(BaseModel):
    pass


class Vitesse(models.Model):
    marche = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    nage = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    vol = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    rampe = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    escalade = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)

    def __str__(self):
        return 'marche({})-nage({})-vol({})-rampe({})-escalade({})'.format(self.marche, self.nage, self.vol, self.rampe, self.escalade)


class Cible(models.Model):
    desc = models.TextField(null=True, blank=True)
    type = models.CharField(null=True, blank=True,
                            default='créature', max_length=50)
    cible = models.IntegerField(null=True, blank=True, default=1)
    zone = models.BooleanField(default=False)
    rayon = models.DecimalField(
        decimal_places=2, max_digits=4, null=True, blank=True)

    def __str__(self):
        if self.zone:
            return f'zone {self.rayon}m'
        if self.cible > 1:
            return f'{self.cible} {self.type}s'
        else:
            return f'{self.cible} {self.type}'


class JetDeSauvegarde(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', blank=True, null=True, related_name='JdS', on_delete=models.CASCADE)
    value = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.caracteristique}+{self.value}'
