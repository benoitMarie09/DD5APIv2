from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.urls import reverse
import re
from model_utils.managers import InheritanceManager

def camel_to_snake(camel):
    camel = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel).lower()

def endpoint_case(snake):
    list = []
    for word in snake.split('_'): 
        if word == 'niveau':
            list.append('niveaux')
        elif word[-1] not in ('s','x'):
            list.append(word+'s')
        else:
            list.append(word)
    return '-'.join(list)+'-detail'


# Model de reference
class BaseModel(models.Model):
    nom = models.CharField(max_length=50)
    index = models.CharField(
        primary_key=True, max_length=50, default='default')
    desc = models.TextField('description', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['index']

    def save(self, *args, **kwargs):
        self.index = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.index

    def get_absolute_url(self):
        return reverse(endpoint_case(camel_to_snake(str(self.__class__.__name__))), kwargs={'pk': self.pk})

# Endpoints


class Race(BaseModel):
    parent_race = models.BooleanField(default=False)
    vitesse = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    taille = models.ForeignKey(
        'Taille', null=True, blank=True, related_name='Race', on_delete=models.CASCADE)
    taille_details = models.TextField(null=True, blank=True)
    age = models.TextField(null=True, blank=True)
    poids = models.TextField(null=True, blank=True)
    bonus_caracteristique = models.ManyToManyField(
        'Caracteristique', blank=True, through='ValeurCaracteristique')
    bonus_caracteristique_option = models.ForeignKey(
        'Option', blank=True, related_name='race_caracteristiques', null=True, on_delete=models.CASCADE)
    maitrises_depart = models.ManyToManyField(
        'Maitrise', blank=True, related_name='race')
    maitrises_option = models.ForeignKey(
        'Option', blank=True, related_name='race_maitrises', null=True, on_delete=models.CASCADE)
    langues = models.ManyToManyField('Langue', blank=True, related_name='race')
    langues_option = models.ForeignKey(
        'Option', blank=True, related_name='race_langues', null=True, on_delete=models.CASCADE)
    langues_desc = models.TextField(null=True, blank=True)
    traits = models.ManyToManyField('Trait', blank=True, related_name='race')
    sorts = models.ManyToManyField('Sort', blank=True, related_name='race')
    sorts_option = models.ForeignKey(
        'Option', blank=True, related_name='race_sorts', null=True, on_delete=models.CASCADE)
    objects = InheritanceManager()



class SousRace(Race):
    race = models.ForeignKey('Race', null=True, blank=True,
                             related_name='sous_race', on_delete=models.CASCADE)


class Maitrise(BaseModel):
    type = models.ForeignKey('CategorieEquipement',
                             blank=True, null=True, on_delete=models.CASCADE)
    ref_equip = models.ForeignKey(
        'Equipement', blank=True, null=True, on_delete=models.CASCADE)
    ref_comp = models.ForeignKey(
        'Competence', blank=True, null=True, on_delete=models.CASCADE)



class Langue(BaseModel):
    CHOIX_TYPE = [
        ('standard', 'standard'),
        ('exotic', 'exotic')
    ]
    type = models.CharField(null=True, blank=True,
                            choices=CHOIX_TYPE, max_length=10)
    race_typiques = models.ManyToManyField('RaceTypique', blank=True)



class Caracteristique(BaseModel):
    pass


class Trait(BaseModel):
    pass


class Alignement(BaseModel):
    abreviation = models.CharField(null=True, blank=True, max_length=2)
    url = models.CharField(null=True, blank=True, max_length=50)



class Historique(BaseModel):
    maitrises_depart = models.ManyToManyField(
        'Maitrise', blank=True, related_name='historique')
    maitrises_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_maitrises', on_delete=models.CASCADE)
    competences = models.ManyToManyField('competence', blank=True)
    langues_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_langues', on_delete=models.CASCADE)
    equipements_depart = models.ManyToManyField(
        'Equipement', blank=True, related_name='historique', through='QuantiteEquipement')
    equipements_options = models.ForeignKey(
        'Option', blank=True, null=True,related_name='historique_equipements', on_delete=models.CASCADE)
    monaie_depart = models.ManyToManyField(
        'Monaie', blank=True, related_name='monaie', through='QuantiteMonaie')
    url = models.CharField(null=True, blank=True, max_length=50)



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

class TypeDegat(BaseModel):
    pass


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


class Etat(BaseModel):
    pass


class Competence(BaseModel):
    caracteristique = models.ForeignKey(
        'Caracteristique', blank=True, null=True, related_name='competences', on_delete=models.CASCADE)

class Don(BaseModel):
    prerequis_caracteristique = models.ForeignKey(
        'PrerequisCaracteristique', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_maitrise = models.ForeignKey(
        'PrerequisMaitrise', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_race = models.ForeignKey(
        'PrerequisRace', null=True, blank=True, related_name='don', on_delete=models.CASCADE)
    prerequis_magie = models.ForeignKey(
        'PrerequisMagie', null=True, blank=True, related_name='don', on_delete=models.CASCADE)

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


class Regle(BaseModel):
    pass


class RegleSousSection(BaseModel):
    regle = models.ForeignKey('Regle', blank=True, null=True,
                              related_name='sous_section', on_delete=models.CASCADE)


# Models qui ne sont pas dans les endpoints


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
        ordering = ['classe','niveau',] 
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


class Taille(BaseModel):
    abreviation = models.CharField(null=True, blank=True, max_length=2)
    def __str__(self):
        return f"{self.nom}({self.abreviation})"



class Personalite(models.Model):
    historique = models.OneToOneField(
        'Historique', null=True, related_name='personalite', on_delete=models.CASCADE)
    domaine = models.ManyToManyField(
        'DomaineHistorique', blank=True, related_name='personalite')
    capacite = models.ManyToManyField(
        'CapaciteHistorique', blank=True, related_name='personalite')
    trait = models.ManyToManyField(
        'TraitHistorique', blank=True, related_name='personalite')
    ideal = models.ManyToManyField(
        'IdealHistorique', blank=True, related_name='personalite')
    lien = models.ManyToManyField(
        'LienHistorique', blank=True, related_name='personalite')
    Defaut = models.ManyToManyField(
        'DefautHistorique', blank=True, related_name='personalite')

    def __str__(self):
        return f"personalité {self.historique}"


class Info(BaseModel):
    pass


class Epuisement(Etat):
    niveau = models.IntegerField(default=1)
    effet = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return f"épuisement(nv{self.niveau})"


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


class Multiclasse(models.Model):
    classe = models.OneToOneField('Classe', on_delete=models.CASCADE)
    prerequis = models.ForeignKey(
        'PrerequisCaracteristique', blank=True, null=True, on_delete=models.CASCADE)
    maitrise = models.ManyToManyField('Maitrise')

    def __str__(self):
        return f'multiclasse {self.classe}'


class Prerequis(models.Model):
    CHOIX_LOGIQUE = [
        ('ou', 'ou'),
        ('et', 'et')
    ]
    logique = models.CharField(
        max_length=2, blank=True, null=True, choices=CHOIX_LOGIQUE)


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


class Degat(models.Model):
    bonus = models.IntegerField(default=0)
    de = models.CharField('dé de dégat', default='1d6', max_length=50)
    type = models.ForeignKey("TypeDegat", blank=True,
                             null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['type']

    def __str__(self):
        if self.bonus == 0:
            return f'{self.de}({self.type.index})'
        return f'{self.de}+{self.bonus}({self.type.index})'


class Soin(models.Model):
    bonus = models.IntegerField(default=0)
    bonus_mod = models.BooleanField(default=False)
    de = models.CharField('dé de dégat', default='1d6', max_length=50)
    type = models.ForeignKey("TypeDegat", blank=True,
                             null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.bonus == 0:
            if self.bonus_mod:
                return f'{self.de}({self.type.index}) + MOD'
        if self.bonus_mod:
            return f'{self.de}+{self.bonus}({self.type.index}) + MOD'
        return f'{self.de}+{self.bonus}({self.type.index})'


class DegatSortEmplacements(models.Model):
    desc = models.TextField(null=True, blank=True)
    emplacement_nv0 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv0')
    emplacement_nv1 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv1')
    emplacement_nv2 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv2')
    emplacement_nv3 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv3')
    emplacement_nv4 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv4')
    emplacement_nv5 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv5')
    emplacement_nv6 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv6')
    emplacement_nv7 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv7')
    emplacement_nv8 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv8')
    emplacement_nv9 = models.ManyToManyField('Degat',blank=True,related_name='emplacement_nv9')

class DegatSortNiveaux(models.Model):
    desc = models.TextField(null=True, blank=True)
    niveau_0 = models.ManyToManyField('Degat',blank=True,related_name='niveau_0')
    niveau_5 = models.ManyToManyField('Degat',blank=True,related_name='niveau_1')
    niveau_11 = models.ManyToManyField('Degat',blank=True,related_name='niveau_2')
    niveau_17 = models.ManyToManyField('Degat',blank=True,related_name='niveau_3')



    
class SoinSortEmplacements(models.Model):
    desc = models.TextField(null=True, blank=True)
    emplacement_nv0 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv0')
    emplacement_nv1 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv1')
    emplacement_nv2 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv2')
    emplacement_nv3 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv3')
    emplacement_nv4 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv4')
    emplacement_nv5 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv5')
    emplacement_nv6 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv6')
    emplacement_nv7 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv7')
    emplacement_nv8 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv8')
    emplacement_nv9 = models.ManyToManyField('Soin',blank=True,related_name='emplacement_nv9')

class Monaie(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)
    desc = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nom


class DefautHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class LienHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class IdealHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class DomaineHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class TraitHistorique(models.Model):
    index = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(null=True, blank=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.index


class CapaciteHistorique(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField('description', null=True, blank=True)

    def __str__(self):
        return self.nom


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


class RaceTypique(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nom


class JetDeSauvegarde(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', blank=True, null=True, related_name='JdS', on_delete=models.CASCADE)
    value = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.caracteristique}+{self.value}'

# Models throught


class QuantiteMonaie(models.Model):
    quantite = models.IntegerField()
    monaie = models.ForeignKey(
        'Monaie', default='Po', null=True, on_delete=models.CASCADE)
    equipement = models.ForeignKey(
        'Equipement', blank=True, null=True, related_name='prix', on_delete=models.CASCADE)
    historique = models.ForeignKey(
        'Historique', blank=True, null=True, related_name='monaie_de_depart', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantite} {self.monaie}"



class QuantiteMonaie_inline(admin.TabularInline):
    model = QuantiteMonaie
    extra = 0


class MonaieAdmin(admin.ModelAdmin):
    inlines = (QuantiteMonaie_inline,)


class QuantiteEquipement(models.Model):
    quantite = models.IntegerField(default=1)
    equipement = models.ForeignKey(
        'Equipement', related_name='quantite', blank=True, null=True, on_delete=models.CASCADE)
    historique = models.ForeignKey(
        'Historique', related_name='quantite_equipement', blank=True, null=True, on_delete=models.CASCADE)
    classe = models.ForeignKey(
        'Classe', related_name='quantite_equipement', blank=True, null=True, on_delete=models.CASCADE)
    pack_equipement = models.ForeignKey(
        'PackEquipementClasse', related_name='contenu_pack', blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.quantite}"


class QuantiteEquipementAventurier(models.Model):
    quantite = models.IntegerField(default=1)
    equipement = models.ForeignKey(
        'EquipementAventurier', related_name='quantite_equipement_aventurier', blank=True, null=True, on_delete=models.CASCADE)
    sac = models.ForeignKey(
        'Sac', related_name='quantite_equipement_aventurier', blank=True, null=True, on_delete=models.CASCADE)

class QuantiteEquipement_inline(admin.TabularInline):
    model = QuantiteEquipement


class PackEquipementClasseAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline,)

class QuantiteEquipementAventurier_inline(admin.TabularInline):
    model = QuantiteEquipementAventurier


class EquipementAventurierAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipementAventurier_inline, QuantiteMonaie_inline)

class SacAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipementAventurier_inline, QuantiteMonaie_inline)

class EquipementAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline, QuantiteMonaie_inline,)


class HistoriqueAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline, QuantiteMonaie_inline,)


class ClasseAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline,)


class QuantiteSpecifique(models.Model):
    valeur = models.DecimalField(
        decimal_places=2, max_digits=4, null=True, blank=True)
    quantite = models.IntegerField(default=1,blank=True, null=True)
    specifique = models.ForeignKey(
        'Specifique', null=True, blank=True, on_delete=models.CASCADE)
    niveau = models.ForeignKey(
        'Niveau', null=True, blank=True,related_name='specifique', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.quantite}"

class QuantiteSpecifique_inline(admin.TabularInline):
    model = QuantiteSpecifique
    extra = 0


class SpecifiqueAdmin(admin.ModelAdmin):
    inlines = (QuantiteSpecifique_inline,)


class NiveauAdmin(admin.ModelAdmin):
    inlines = (QuantiteSpecifique_inline,)


class ValeurCaracteristique(models.Model):
    valeur = models.IntegerField(default=1)
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='valeur_caract', blank=True, null=True, on_delete=models.CASCADE)
    race = models.ForeignKey(
        'Race', related_name='caracteristique', blank=True, null=True, on_delete=models.CASCADE)
    prerequis = models.ForeignKey(
        'PrerequisCaracteristique', related_name='valeur_caract', blank=True, null=True, on_delete=models.CASCADE)
    monstre = models.ForeignKey(
        'Monstre', related_name='valeur_caract1', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: +{}'.format(self.caracteristique, self.valeur)


class ValeurCaracteristique_inline(admin.TabularInline):
    model = ValeurCaracteristique
    extra = 0


class CaracteristiqueAdmin(admin.ModelAdmin):
    inlines = (ValeurCaracteristique_inline,)


class RaceAdmin(admin.ModelAdmin):
    inlines = (ValeurCaracteristique_inline,)


class PrerequisCaracteristiqueAdmin(admin.ModelAdmin):
    inlines = (ValeurCaracteristique_inline,)


class MonstreAdmin(admin.ModelAdmin):
    inlines = (ValeurCaracteristique_inline,)


# class NbChoix_inline(admin.TabularInline):
#     model = NbChoix
#     extra = 1


# class QuantiteEquipement_inline(admin.TabularInline):
#     model = QuantiteEquipement
#     extra = 1


# class ClasseAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }


# class PJAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }
