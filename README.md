# Suivi des stages — projet fil rouge du cours Django

Application de gestion des stages de l'IFNTI de Sokodé : les entreprises publient des offres,
les étudiants candidatent, les stages retenus donnent lieu à une convention et à une évaluation.

C'est le projet que nous construisons ensemble, séance après séance, pendant tout le semestre.
Ce dépôt ne contient **que le code** ; les énoncés de TP sont distribués sur Moodle.

## Prérequis

- Ubuntu 24.04 LTS ou 22.04 LTS ;
- `git` ;
- `uv`, qui ne s'installe pas par `apt` :

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

`uv` se charge du reste, Python compris : ni `apt install python3.14`, ni `pip`, ni `virtualenv`.
Le fichier `.python-version` épingle Python 3.14 et `uv` l'installe au besoin — toute la classe
travaille ainsi sur la même version, donc sur les mêmes messages d'erreur.

## Démarrer

```bash
git clone https://github.com/vianney-g/ifnti_django_projet.git
cd ifnti_django_projet
uv sync                                   # crée l'environnement et installe les dépendances
uv run manage.py migrate                  # crée la base SQLite locale
uv run manage.py loaddata demo            # facultatif : un jeu de données de démonstration
uv run manage.py createsuperuser          # votre compte d'administration
uv run manage.py runserver
```

Puis <http://localhost:8000/entreprises/> pour la liste, <http://localhost:8000/admin/> pour
l'administration.

Les tests :

```bash
uv run pytest
```

## Les points de reprise

**Une séance manquée ne doit bloquer personne.** Chaque TP a donc deux tags :

| tag | état du code |
|---|---|
| `tpN-depart` | ce dont vous avez besoin pour commencer le TP N |
| `tpN-corrige` | le code tel qu'il devrait être à la fin du TP N |

Si vous avez manqué une séance, ou si votre code est parti de travers, repartez du tag de départ
du TP du jour :

```bash
git fetch --tags
git switch -c tp3 tp3-depart   # une branche de travail à partir du tag
uv sync                        # les dépendances changent d'un TP à l'autre
```

Travaillez sur une branche, comme ci-dessus : `git checkout tp3-depart` seul vous laisse en
« HEAD détachée », et vos commits y seraient perdus.

Ne regardez un `tpN-corrige` qu'après avoir cherché. Le TP compte moins que ce que vous y
comprenez, et la soutenance de fin de semestre porte sur *votre* dépôt et *votre* historique git.

## État du dépôt

Le code s'arrête à la fin de la séance Modéliser le domaine : le modèle de données du suivi des
stages, découpé en un fichier par modèle dans `stages/models/`, entièrement administrable.
La convention de stage et l'évaluation arriveront plus tard, avec les séances qui en ont besoin.

`uv run manage.py loaddata demo` charge des entreprises, des étudiants, des offres et quelques
stages fictifs, pour travailler sur une base qui ne soit pas vide. Les tags suivants arrivent au
fil des séances.
