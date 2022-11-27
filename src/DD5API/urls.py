from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from data.views import *

router = routers.SimpleRouter()

router.register('historique', HistoriqueViewset, basename='historique')
router.register('equipement', EquipementViewset, basename='equipement')
router.register('arme', ArmeViewset, basename='arme')
router.register('armure', ArmureViewset, basename='armure')
router.register('outil', OutilViewset, basename='outil')
router.register('race', RaceViewset, basename='race')
router.register('competence', CompetenceViewset, basename='competence')
router.register('classe', ClasseViewset, basename='classe')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
