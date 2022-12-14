from django.db import models
from .base import BaseModel
from model_utils.managers import InheritanceManager


class Equipement(BaseModel):
    prix_objet = models.ManyToManyField(
        'Monaie', blank=True, through='QuantiteMonaie')
    poids = models.DecimalField(
        decimal_places=3, max_digits=5, null=True, blank=True)
    categorie_equipement = models.ForeignKey(
        "CategorieEquipement",default='outil', on_delete=models.CASCADE)
    objects = InheritanceManager()


class EquipementAventurier(Equipement):
    categorie_equipement_aventurier = models.ForeignKey(
        "CategorieEquipement",default='outil-dartisan', on_delete=models.CASCADE)


class Sac(Equipement):
    contenu =  models.ManyToManyField("EquipementAventurier", blank=True, through='QuantiteEquipementAventurier', related_name='sac')


class CategorieEquipement(BaseModel):
    pass


class Arme(Equipement):
    categorie_arme = models.ForeignKey(
        "CategorieEquipement", blank=True, null=True,related_name='categorie_arme', on_delete=models.CASCADE)
    categorie_portee = models.ForeignKey(
        "CategorieEquipement", blank=True, null=True,related_name='categorie_portee', on_delete=models.CASCADE)
    categorie_arme_portee = models.ForeignKey(
        "CategorieEquipement",default='arme-de-guerre-de-corps-a-corps',related_name='categorie_arme_portee', on_delete=models.CASCADE)
    portee = models.ManyToManyField("Portee", blank=True)
    degat_une_main = models.ForeignKey(
        "Degat", null=True, blank=True, related_name='degat1main', on_delete=models.CASCADE)
    degat_deux_mains = models.ForeignKey(
        "Degat", null=True, blank=True, related_name='degat2mains', on_delete=models.CASCADE)
    degat_distance = models.ForeignKey(
        "Degat", null=True, blank=True, related_name='degat_distance', on_delete=models.CASCADE)
    propriete = models.ManyToManyField('ProprieteArme', blank=True)
    special = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.categorie_arme_portee.index == 'arme-courante-de-corps-a-corps':
            self.categorie_arme=CategorieEquipement.objects.get(index= 'arme-courante')
            self.categorie_portee = CategorieEquipement.objects.get(index= 'arme-de-corps-a-corps')
        elif self.categorie_arme_portee.index == 'arme-de-guerre-a-distance':
            self.categorie_arme=CategorieEquipement.objects.get(index= 'arme-de-guerre')
            self.categorie_portee = CategorieEquipement.objects.get(index= 'arme-a-distance')
        elif self.categorie_arme_portee.index == 'arme-courante-a-distance':
            self.categorie_arme=CategorieEquipement.objects.get(index= 'arme-courante')
            self.categorie_portee = CategorieEquipement.objects.get(index= 'arme-a-distance')
        else:
            self.categorie_arme=CategorieEquipement.objects.get(index= 'arme-de-guerre')
            self.categorie_portee = CategorieEquipement.objects.get(index= 'arme-de-corps-a-corps')
        return super().save(*args, **kwargs)
    


class Armure(Equipement):
    categorie_armure = models.ForeignKey(
        "CategorieEquipement", blank=True, null=True,related_name='categorie_armure', on_delete=models.CASCADE)
    CA = models.ForeignKey('ClasseArmure', null=True,
                           blank=True, on_delete=models.CASCADE)
    force_min = models.IntegerField(default=0)
    desaventage_discretion = models.BooleanField(default=False)



class Vehicule(Equipement):
    categorie = models.CharField(
        "categorie de véhicule", null=True, blank=True, max_length=50)
    capacite = models.IntegerField(null=True, blank=True)
    vitesse = models.IntegerField(null=True, blank=True)

class ProprieteArme(BaseModel):
    pass


class ClasseArmure(models.Model):
    base = models.IntegerField(default=11)
    dex_bonus = models.BooleanField(default=True)
    max_bonus = models.IntegerField(default=None, null=True, blank=True)
    bonus_CA = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self):
        dex = ""
        bonus = ""
        base = ""
        if self.base:
            base = f'{self.base}'
        if self.dex_bonus:
            dex = f' + Mod.Dex'
        if self.max_bonus:
            dex = dex+f'(max +{self.max_bonus})'
        if self.bonus_CA:
            bonus = f'+{self.bonus_CA}'
        return base+dex+bonus


class Portee(models.Model):
    min = models.FloatField(null=True, blank=True)
    max = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.max == 0:
            return "personnelle"
        if self.max == 1.5:
            return "càc"
        if self.max == 3:
            return "càc 3m"
        return f"{self.min}-{self.max}"


class Monaie(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)
    desc = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nom
