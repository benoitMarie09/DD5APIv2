# DD5API

API en français pour le jeu de rôle Donjon Dragon édition 5

## Instalation

cloner le repo :

```console
git clone https://github.com/benoitMarie09/DD5API.git
```

À la racine du depot DD5API créer un environement virtuel:

```console
/DD5API$ python3 -m venv .env
```

DD5API$ Activer l'environement virtuel:

```console
/DD5API$ source .env/bin/activate
```

DD5API$ Installer les dépendances:

```console
/DD5API$ pip install -r requirement.txt
```

## Lancer l'API

Dans le dossier src lancer le serveur:

```console
/DD5API/src$ python3 manage.py runserver
```

## Mode d'emploi

#### Endpoints

Avec adresse local

Les classes:  
http://127.0.0.1:8000/api/classe/<pk>

Les races:  
http://127.0.0.1:8000/race/<pk>

Les historiques:  
http://127.0.0.1:8000/historique/<pk>

Les compétences:  
http://127.0.0.1:8000/competence/<pk>

L'equipement:  
http://127.0.0.1:8000/equipement/<pk>

Les armes:  
http://127.0.0.1:8000/equipement/arme/\<pk\>

Les armures:  
http://127.0.0.1:8000/equipement/armure/<pk>

Les outils:  
http://127.0.0.1:8000/equipement/outil/<pk>

_Ajouter `/?format=json` pour avoir un json._
