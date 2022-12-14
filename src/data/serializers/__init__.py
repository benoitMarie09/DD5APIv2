from rest_framework.serializers import ModelSerializer, Field, RelatedField, StringRelatedField

from .base.base import BaseSerializers

from .alignement.list import AlignementListSerializers
from .alignement.detail import AlignementDetailSerializers

from .caracteristique.list import CaracteristiqueListSerializers
from .caracteristique.detail import CaracteristiqueDetailSerializers

from .classe.list import CapaciteListSerializers, NiveauListSerializers, PackEquipementClasseListSerializers, InfoListSerializers, SousClasseListSerializers, ClasseListSerializers
from .classe.detail import CapaciteDetailSerializers, ClasseDetailSerializers, SousClasseSerializers

from .competence.list import CompetenceListSerializers
from .competence.detail import CompetenceDetailSerializers

from .degat.list import TypeDegatListSerializers
from .degat.detail import TypeDegatDetailSerializers, DegatSortEmplacementsSerializer, DegatSortNiveauxSerializer, SoinSortEmplacementsSerializer

from .don.list import DonSerializers
# from don.detail import 

from .equipement.list import SacListSerializers, EquipementAventurierListSerializers, CategorieEquipementListSerializers, ProprieteArmeListSerializers, ArmeListSerializers, ArmureListSerializers, EquipementListSerializers, VehiculeListSerializers
from .equipement.detail import SacDetailSerializers, EquipementAventurierDetailSerializers, CategorieEquipementDetailSerializers, ProprieteArmeDetailSerializers, EquipementDetailSerializers, ArmeDetailSerializers, ArmureDetailSerializers, VehiculeDetailSerializers

from .etat.list import EtatListSerializers
from .etat.detail import EtatDetailSerializers

from .historique.list import HistoriqueListSerializers
from .historique.detail import HistoriqueDetailSerializers

from .langue.list import LangueListSerializers
from .langue.detail import LangueDetailSerializers

from .maitrise.list import MaitriseListSerializers
from .maitrise.detail import MaitriseDetailSerializers

from .monstre.list import MonstreSerializers, CapaciteMonstreSerializers
# from monstre.detail import

from .option.list import OptionListSerializer

from .race.list import RaceMaitrisesOptionsList, RaceListSerializers, SousRaceListSerializers, TraitListSerializers
from .race.detail import RaceDetailSerializers, OptionPackDetailSerializer, IncantationDetailSerializers, NiveauDetailSerializers, TraitDetailSerializers, SousRaceDetailSerializers

from .regle.list import RegleSerializers, RegleSousSectionSerializers

from .sort.list import SortListSerializers, EcoleMagieListSerializers
from .sort.detail import SortDetailSerializers, EcoleMagieDetailSerializers
