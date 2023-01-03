# DD5API

API en français pour le jeu de rôle Donjon Dragon édition 5

## Installation

cloner le repo :

```console
git clone https://github.com/benoitMarie09/DD5APIv2.git
```

**À la racine du depot DD5API créer un environement virtuel:**


*/DD5API$* ```console python3 -m venv .env ```


**Activer l'environement virtuel:**


*/DD5API$* ```console source .env/bin/activate ```


**Installer les dépendances:**

*/DD5API$* ```console pip install -r requirement.txt ```

## Lancer l'API

Dans le dossier src lancer le serveur:

```console
/DD5API/src$ python3 manage.py runserver
```

## Mode d'emploi

#### Endpoints

Avec adresse local

Les classes:

> `http://127.0.0.1:8000/api/classe/<pk>`

Les races:

> `http://127.0.0.1:8000/race/<pk>`

Les historiques:

> `http://127.0.0.1:8000/historique/<pk>`

Les compétences:

> `http://127.0.0.1:8000/competence/<pk>`

L'equipement:

> `http://127.0.0.1:8000/equipement/<pk>`

Les armes:

> `http://127.0.0.1:8000/equipement/arme/<pk>`

Les armures:

> `http://127.0.0.1:8000/equipement/armure/<pk>`

Les outils:

> `http://127.0.0.1:8000/equipement/outil/<pk>`

**Ajouter `/?format=json` pour avoir un json.**

## Exemples

info barbare en json:

> `http://127.0.0.1:8000/api/classe/barbare/?format=json`

info toutes les competences en json:

> `http://127.0.0.1:8000/competence/?format=json`
