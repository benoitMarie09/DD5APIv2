from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple




class Historique(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True)
    competences = models.ManyToManyField(
        'Competence', related_name='historiques')
    maitrise = models.ManyToManyField('Outil')
    langue = models.ManyToManyField('Langue')
    po = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id


class QuantiteEquipement(models.Model):
    historique = models.ForeignKey(
        'Historique', related_name='quantite_equipement', on_delete=models.SET_NULL, null=True)
    equipement = models.ForeignKey(
        'Equipement', related_name='quantite_equipement', on_delete=models.SET_NULL, null=True)
    quantite = models.IntegerField(default=1)


class Equipement(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True, blank=True)
    prix = models.FloatField(null=True, blank=True)
    poids = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.id


class Arme(Equipement):

    CONTONDANT = 'CTD'
    PERFORANT = 'PRF'
    TRANCHANT = 'TRC'

    DEGAT_TYPE_CHOICES = (
        (CONTONDANT, 'Contondant'),
        (PERFORANT, 'Cerforant'),
        (TRANCHANT, 'Tranchant'),
        (None, '(Aucun)')
    )

    degat = models.CharField(null=True,
                             blank=True, max_length=5)
    type_degat = models.CharField(null=True,
                                  blank=True, max_length=3, choices=DEGAT_TYPE_CHOICES)
    propriete = models.ManyToManyField(
        'ProprieteArme')
    portee_min = models.FloatField(null=True, blank=True)
    portee_max = models.FloatField(null=True, blank=True)


class ProprieteArme(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.id


class Armure(Equipement):
    MOD_1 = 1
    MOD_2 = 2
    MOD_DEXT_CHOICES = (
        (MOD_1, 'mod.dex'),
        (MOD_2, 'mod.dex(+2max)'),
        (None, 'aucun')
    )
    LEGERE = 'LGR'
    INTERMEDIAIRE = 'INT'
    LOURDE = 'LRD'
    BOUCLIER = 'BCL'
    CATEGORIES_CHOICES = (
        (LEGERE, 'Légère'),
        (INTERMEDIAIRE, 'Intermédiaire'),
        (LOURDE, 'Lourde'),
        (BOUCLIER, 'Bouclier')
    )

    CA = models.IntegerField(null=True, blank=True)
    mod_dext = models.IntegerField(
        null=True, blank=True, choices=MOD_DEXT_CHOICES)
    discretion_desavantage = models.BooleanField(default=False)
    force_min = models.IntegerField(null=True, blank=True)
    categorie = models.CharField(max_length=3, choices=CATEGORIES_CHOICES)


class Langue(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.id


class Outil(Equipement):
    INSTRUMENT = 'INS'
    JEU = 'JEU'
    KIT = 'KIT'
    OUTIL = 'OUT'
    VEHICULE = 'VEH'

    TYPE_CHOICES = (
        (INSTRUMENT, 'Instrument de musique'),
        (JEU, 'jeu'),
        (KIT, 'kit'),
        (OUTIL, "outils d'artisan"),
        (VEHICULE, 'vehicule')
    )
    type = models.CharField(default=OUTIL, max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return self.id


class NbChoix(models.Model):
    valeur = models.IntegerField(default=1)
    choix = models.ForeignKey(
        'Choix', related_name='valeur', on_delete=models.CASCADE)
    historique = models.ForeignKey(
        'Historique', null=True, on_delete=models.CASCADE)


class Choix(models.Model):
    id = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.id


class RaceCapacite(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.id


class Race(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    desc = models.TextField(null=True, blank=True)
    taille_max = models.IntegerField(null=True, blank=True)
    taille_min = models.IntegerField(null=True, blank=True)
    vitesse = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    bonus_caracteristique = models.ManyToManyField(
        'Caracteristique', through='BonusCaracteristique')
    capacite = models.ManyToManyField('RaceCapacite')
    famille = models.CharField(null=True, blank=True, max_length=20)
    #sorts = manytomany

    def __str__(self):
        return self.id


class BonusCaracteristique(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='bonus_caract', on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(
        'Race', related_name='bonus_caract', on_delete=models.SET_NULL, null=True)
    valeur = models.IntegerField(default=1)

    def __str__(self):
        return '{}:{}+{}'.format(self.race, self.caracteristique, self.valeur)


class ValeurCaracteristique(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='valeur_caract', on_delete=models.SET_NULL, null=True)
    PJ = models.ForeignKey(
        'PJ', related_name='valeur_caract', on_delete=models.SET_NULL, null=True)
    valeur = models.IntegerField(default=10)


class Caracteristique(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    nom = models.CharField(null=True, max_length=20)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.id


class Competence(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    desc = models.TextField(null=True)
    caracteristique = models.ForeignKey(
        'Caracteristique', null=True, related_name='competences', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Classe(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    desc = models.TextField(null=True)
    dv = models.IntegerField(null=True)
    choix_competences = models.ManyToManyField(
        'Competence', related_name='classes')
    nb_competences = models.IntegerField(default=2)
    jets_sauvegarde = models.ManyToManyField('Caracteristique')

    def __str__(self):
        return self.id


class PJ(models.Model):
    nom = models.CharField(null=True, max_length=100)
    race = models.ForeignKey(
        'Race', null=True, related_name='PJs', on_delete=models.CASCADE)
    classe = models.ForeignKey(
        'Classe', null=True, related_name='PJs', on_delete=models.CASCADE)
    maitrise_competences = models.ManyToManyField('Competence')
    historique = models.ForeignKey(
        'Historique', null=True, related_name='PJs', on_delete=models.CASCADE)

    force = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    dexterite = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    sagesse = models.IntegerField(null=True, blank=True)
    charisme = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.nom, self.classe)

    def save(self, *args, **kwargs):
        if self.force is None:
            if self.race:
                print(self.race)
                try:
                    self.force = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='for').valeur
                except:
                    self.force = 10
        if self.constitution is None:
            if self.race:
                try:
                    self.constitution = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='con').valeur
                except:
                    self.constitution = 10
        if self.dexterite is None:
            if self.race:
                try:
                    self.dexterite = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='dex').valeur
                except:
                    self.dexterite = 10
        if self.intelligence is None:
            if self.race:
                try:
                    self.intelligence = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='int').valeur
                except:
                    self.intelligence = 10
        if self.sagesse is None:
            if self.race:
                try:
                    self.sagesse = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='sag').valeur
                except:
                    self.sagesse = 10
        if self.charisme is None:
            if self.race:
                try:
                    self.charisme = 10 + BonusCaracteristique.objects.get(
                        race=self.race, caracteristique='cha').valeur
                except:
                    self.charisme = 10

        super(PJ, self).save(*args, **kwargs)

# Gestion des formulaire admin pour le m2m


class NbChoix_inline(admin.TabularInline):
    model = NbChoix
    extra = 1


class QuantiteEquipement_inline(admin.TabularInline):
    model = QuantiteEquipement
    extra = 1


class BonusCaracteristique_inline(admin.TabularInline):
    model = BonusCaracteristique
    extra = 1


class HistoriqueAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline, NbChoix_inline)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class EquipementAdmin(admin.ModelAdmin):
    inlines = (QuantiteEquipement_inline,)


class RaceAdmin(admin.ModelAdmin):
    inlines = (BonusCaracteristique_inline,)


class CaracteristiqueAdmin(admin.ModelAdmin):
    inlines = (BonusCaracteristique_inline,)


class ArmeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class ChoixAdmin(admin.ModelAdmin):
    inlines = (NbChoix_inline,)


class ClasseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class PJAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
