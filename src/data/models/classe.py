from django.db import models
from .base import BaseModel
from django.urls import reverse


class Classe(BaseModel):
    pv = models.IntegerField(default=8)
    maitrises = models.ManyToManyField(
        'Maitrise', blank=True, related_name='classe')
    options_maitrises = models.ForeignKey(
        'Option', null=True, blank=True,related_name='classe_maitrises', on_delete=models.CASCADE)
    jets_sauvegardes = models.ManyToManyField(
        'Caracteristique', blank=True, related_name='classe')
    options_competences = models.ForeignKey(
        'Option', null=True, blank=True, related_name='classe_competences', on_delete=models.CASCADE)
    equipements_depart = models.ManyToManyField(
        'Equipement', blank=True, through='QuantiteEquipement', related_name='classe')
    equipements_options = models.ForeignKey(
        'Option', null=True, blank=True,related_name='classe_equipements', on_delete=models.CASCADE)
    incantation = models.OneToOneField(
        'Incantation', null=True, blank=True, related_name='classe', on_delete=models.CASCADE)
    sorts = models.ManyToManyField('Sort', blank=True, related_name='classe')
    niveaux = models.ManyToManyField('Niveau',related_name='classe', blank=True)


class PackEquipementClasse(BaseModel):
    contenu = models.ManyToManyField('Equipement', blank=True, related_name='Pack',through='QuantiteEquipement')
    options = models.ManyToManyField('Option', blank=True, related_name='Pack')


class Incantation(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    caracteristique = models.ForeignKey(
        'Caracteristique', blank=True, null=True, on_delete=models.CASCADE)
    info = models.ManyToManyField('Info', blank=True)
    def __str__(self):
        return f"{self.nom}"


class Info(BaseModel):
    pass


class SousClasse(BaseModel):
    classe = models.ForeignKey('Classe', blank=True, null=True,
                               related_name='sous_classe', on_delete=models.CASCADE)
    type_option = models.CharField(max_length=50, blank=True, null=True)
    sorts = models.ManyToManyField(
        'Sort', blank=True, related_name='sous_classe')


class NiveauxClasse(BaseModel):
    classe = models.OneToOneField(
        'Classe', null=True, blank=True, related_name='niveau', on_delete=models.CASCADE)
    sous_classe = models.OneToOneField(
        'SousClasse', null=True, blank=True, related_name='niveau', on_delete=models.CASCADE)
    niveaux = models.ManyToManyField(
        'Niveau', blank=True, related_name='niveaux_classe')


class Capacite(BaseModel):
    classe = models.ForeignKey(
        'Classe', null=True, blank=True, related_name='capacite', on_delete=models.CASCADE)
    sous_classe = models.ForeignKey(
        'SousClasse', null=True, blank=True, related_name='capacite', on_delete=models.CASCADE)
    option = models.ForeignKey('Option', blank = True, null = True, on_delete=models.CASCADE)

class Niveau(BaseModel):
    niveau = models.IntegerField(default=1)
    bonus_caracteristique = models.IntegerField(default=0)
    bonus_maitrise = models.IntegerField(default=2)
    capacite = models.ManyToManyField(
        'Capacite', blank=True, related_name='niveau')
    emplacements_sorts = models.ForeignKey(
        'EmplacementSort', blank=True, null=True, related_name='niveau', on_delete=models.CASCADE)
    specifique_classe = models.ManyToManyField(
        'Specifique', blank=True, through='QuantiteSpecifique')
    class Meta:
        ordering = ['classe'] 
    def get_absolute_url(self):
        return reverse('classes-niveau', args=[self.classe.all()[0].index,self.niveau])

class EmplacementSort(models.Model):
    sort_connu = models.IntegerField(default=None, null=True, blank=True)
    nv_0 = models.IntegerField(default=0)
    nv_1 = models.IntegerField(default=0)
    nv_2 = models.IntegerField(default=0)
    nv_3 = models.IntegerField(default=0)
    nv_4 = models.IntegerField(default=0)
    nv_5 = models.IntegerField(default=0)
    nv_6 = models.IntegerField(default=0)
    nv_7 = models.IntegerField(default=0)
    nv_8 = models.IntegerField(default=0)
    nv_9 = models.IntegerField(default=0)

    def __str__(self):
        return '{}-{}-{}-{}-{}-{}-{}-{}-{}-{}'.format(self.nv_0, self.nv_1, self.nv_2, self.nv_3, self.nv_4, self.nv_5, self.nv_6, self.nv_7, self.nv_8, self.nv_9)


class Specifique(models.Model):
    nom = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nom



class Prerequis(models.Model):
    CHOIX_LOGIQUE = [
        ('ou', 'ou'),
        ('et', 'et')
    ]
    logique = models.CharField(
        max_length=2, blank=True, null=True, choices=CHOIX_LOGIQUE)


class Multiclasse(models.Model):
    classe = models.OneToOneField('Classe', on_delete=models.CASCADE)
    prerequis = models.ForeignKey(
        'PrerequisCaracteristique', blank=True, null=True, on_delete=models.CASCADE)
    maitrise = models.ManyToManyField('Maitrise')

    def __str__(self):
        return f'multiclasse {self.classe}'
        

class PrerequisCaracteristique(Prerequis):
    caracteristique = models.ManyToManyField(
        'Caracteristique', blank=True, through='ValeurCaracteristique', related_name='prerequis')

    def __str__(self):
        for item in self.caracteristique:
            name = name + f"{self.logique} {item.index}"
        return name


class PrerequisMaitrise(models.Model):
    maitrise = models.ManyToManyField('Maitrise', blank=True)

    def __str__(self):
        for item in self.maitrise:
            name = name + f"{self.logique} {item.index}"
        return name


class PrerequisRace(models.Model):
    race = models.ManyToManyField('Race', blank=True)

    def __str__(self):
        for item in self.race:
            name = name + f"{self.logique} {item.index}"
        return name


class PrerequisMagie(models.Model):
    desc = models.TextField(null=True, blank=True)



