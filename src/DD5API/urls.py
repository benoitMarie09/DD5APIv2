from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from data.views import *

router = routers.SimpleRouter()

router.register('alignements', AlignementViewset, basename='alignements')
router.register('armures', ArmureViewset, basename='armures')
router.register('capacites', CapaciteViewset, basename='capacites')
router.register('capacites-monstres', CapaciteMonstreViewset, basename='capacites-monstres')
router.register('caracteristiques', CaracteristiqueViewset, basename='caracteristiques')
router.register('categories-equipements', CategorieEquipementViewset, basename='categories-equipements')
router.register('classes', ClasseViewset, basename='classes')
router.register('competences', CompetenceViewset, basename='competences')
router.register('classes', ClasseViewset, basename='classes')
router.register('competences', CompetenceViewset, basename='competences')
router.register('equipements', EquipementViewset, basename='equipements')
router.register('packs-equipements', PackEquipementViewset, basename='packs-equipements')
router.register('etats', EtatViewset, basename='etats')
router.register('historiques', HistoriqueViewset, basename='historiques')
router.register('incantations', IncantationViewset, basename='incantations')
router.register('langues', LangueViewset, basename='langues')
router.register('maitrises', MaitriseViewset, basename='maitrises')
router.register('monstres', MonstreViewset, basename='monstres')
router.register('niveaux', NiveauxClasseViewset, basename='niveaux')
router.register('proprietes-armes', ProprieteArmeViewset, basename='proprietes-armes')
router.register('races', RaceViewset, basename='races')
router.register('races', RaceViewset, basename='races')
router.register('regles', RegleViewset, basename='regles')
router.register('regles-sous-sections', RegleSousSectionViewset, basename='regles-sous-sections')
router.register('sous-classes', SousClasseViewset, basename='sous-classes')
router.register('sous-races', SousRaceViewset, basename='sous-races')
router.register('traits', TraitViewset, basename='traits')
router.register('types-degats', TypeDegatViewset, basename='types-degats')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
