from django.contrib import admin
from .models import *


class QuantiteMonaie_inline(admin.TabularInline):
    model = QuantiteMonaie
    extra = 0


class MonaieAdmin(admin.ModelAdmin):
    inlines = (QuantiteMonaie_inline,)

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

class QuantiteSpecifique_inline(admin.TabularInline):
    model = QuantiteSpecifique
    extra = 0


class SpecifiqueAdmin(admin.ModelAdmin):
    inlines = (QuantiteSpecifique_inline,)


class NiveauAdmin(admin.ModelAdmin):
    inlines = (QuantiteSpecifique_inline,)

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




admin.site.register(Alignement)
admin.site.register(Arme,EquipementAdmin)
admin.site.register(Armure, EquipementAdmin)
admin.site.register(EquipementAventurier, EquipementAventurierAdmin)
admin.site.register(Option)
admin.site.register(PackEquipementClasse, PackEquipementClasseAdmin)
admin.site.register(Sac, SacAdmin)
admin.site.register(Capacite)
admin.site.register(CapaciteMonstre)
admin.site.register(Caracteristique, CaracteristiqueAdmin)
admin.site.register(CategorieEquipement)
admin.site.register(Classe,ClasseAdmin)
admin.site.register(Competence)
admin.site.register(Don)
admin.site.register(EcoleMagie)
admin.site.register(Equipement,EquipementAdmin)
admin.site.register(Etat)
admin.site.register(Historique,HistoriqueAdmin)
admin.site.register(Incantation)
admin.site.register(Langue)
admin.site.register(Maitrise)
admin.site.register(Monstre, MonstreAdmin)
admin.site.register(NiveauxClasse)
admin.site.register(ProprieteArme)
admin.site.register(Race, RaceAdmin)
admin.site.register(Regle)
admin.site.register(RegleSousSection)
admin.site.register(Sort)
admin.site.register(SousClasse)
admin.site.register(SousRace, RaceAdmin)
admin.site.register(Trait)
admin.site.register(TypeDegat)
admin.site.register(Niveau,NiveauAdmin)
admin.site.register(ActionMonstre)
admin.site.register(CapaciteHistorique)
admin.site.register(Cible)
admin.site.register(ClasseArmure)
admin.site.register(Composante)
admin.site.register(DefautHistorique)
admin.site.register(Degat)
admin.site.register(DegatSortEmplacements)
admin.site.register(DegatSortNiveaux)
admin.site.register(SoinSortEmplacements)
admin.site.register(DomaineHistorique)
admin.site.register(EmplacementSort)
admin.site.register(Epuisement)
admin.site.register(IdealHistorique)
admin.site.register(Info)
admin.site.register(LienHistorique)
admin.site.register(Monaie)
admin.site.register(Multiclasse)
admin.site.register(Personalite)
admin.site.register(Portee)
admin.site.register(Prerequis)
admin.site.register(PrerequisCaracteristique, PrerequisCaracteristiqueAdmin)
admin.site.register(PrerequisMagie)
admin.site.register(PrerequisMaitrise)
admin.site.register(PrerequisRace)
admin.site.register(RaceTypique)
admin.site.register(SensMonstre)
admin.site.register(Specifique,SpecifiqueAdmin)
admin.site.register(Taille)
admin.site.register(TraitHistorique)
admin.site.register(Vehicule, EquipementAdmin)
admin.site.register(Vitesse)
admin.site.register(JetDeSauvegarde)
admin.site.register(QuantiteEquipement)
admin.site.register(QuantiteMonaie)
admin.site.register(QuantiteSpecifique)
admin.site.register(ValeurCaracteristique)



