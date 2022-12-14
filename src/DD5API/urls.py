from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from data.views import *
from rest_framework.routers import Route, DynamicRoute, DefaultRouter

class CustomReadOnlyRouter(DefaultRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]


router = DefaultRouter()
customRouter = CustomReadOnlyRouter()
router.register('alignements', AlignementViewset, basename='alignements')
router.register('capacites', CapaciteViewset, basename='capacites')
router.register('capacites-monstres', CapaciteMonstreViewset, basename='capacites-monstres')
router.register('caracteristiques', CaracteristiqueViewset, basename='caracteristiques')
router.register('categories-equipements', CategorieEquipementViewset, basename='categories-equipements')
router.register('classes', ClasseViewset, basename='classes')
router.register('competences', CompetenceViewset, basename='competences')
customRouter.register('classes', ClasseViewset, basename='classes')
router.register('equipements', EquipementViewset, basename='equipements')
router.register('equipements', EquipementViewset, basename='armes')
router.register('equipements', EquipementViewset, basename='armures')
router.register('equipements', EquipementViewset, basename='vehicules')
router.register('equipements', EquipementViewset, basename='equipements-aventuriers')
router.register('equipements', EquipementViewset, basename='sacs')
router.register('etats', EtatViewset, basename='etats')
router.register('historiques', HistoriqueViewset, basename='historiques')
router.register('langues', LangueViewset, basename='langues')
router.register('maitrises', MaitriseViewset, basename='maitrises')
router.register('monstres', MonstreViewset, basename='monstres')
router.register('proprietes-armes', ProprieteArmeViewset, basename='proprietes-armes')
router.register('races', RaceViewset, basename='races')
router.register('regles', RegleViewset, basename='regles')
router.register('regles-sous-sections', RegleSousSectionViewset, basename='regles-sous-sections')
router.register('sous-classes', SousClasseViewset, basename='sous-classes')
router.register('sous-races', SousRaceViewset, basename='sous-races')
router.register('traits', TraitViewset, basename='traits')
router.register('types-degats', TypeDegatViewset, basename='types-degats')
router.register('sorts', SortViewset, basename='sorts')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
