#!/usr/bin/env python3

import os
import sys

USAGE_STRING = """usage : guitte [--version] [--help] [-C <path>] [-c name=value]
       [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
       [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
       [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
       <command> [<args>]

Ci-dessous les commandes Guitte habituelles dans diverses situations :

démarrer une zone de travail (voir aussi : git help tutorial)
  copie-colle      Cloner un dépôt dans un nouveau répertoire
  initialisation   Créer un dépôt Git vide ou réinitialiser un existant

travailler sur la modification actuelle (voir aussi : git help revisions)
  ajout            Ajouter le contenu de fichiers dans l'index
  déplace          Déplacer ou renommer un fichier, un répertoire, ou un lien symbolique
  réinitialisation Réinitialiser la TÊTE courante à l'état spécifié
  enlève           Supprimer des fichiers de la copie de travail et de l'index

examiner l'historique et l'état (voir aussi : git help revisions)
  couper-en-deux   Trouver par recherche dichotomique la modification qui a introduit un bogue
  de-raisin        Afficher les lignes correspondant à un motif
  bûche            Afficher l'historique des validations
  chaud            Afficher différents types d'objets
  état             Afficher le statut de la copie de travail

agrandir, marquer et modifier votre historique
  rameau           Lister, créer ou supprimer des branches
  change-arbre     Basculer de branche ou restaurer la copie de travail
  commettre        Enregistrer les modifications dans le dépôt
  différence       Afficher les changements entre les validations, entre validation et copie de travail, etc
  fusion           Fusionner deux ou plusieurs historiques de développement ensemble
  refais           Réapplication des validations sur le sommet de l'autre base
  graffiti         Créer, lister, supprimer ou vérifier un objet d'étiquette signé avec GPG
  cueillette-de-cerises Applique les changements introduits par certaines validations prééxistantes

collaborer (voir aussi : git help workflows)
  récupère         Télécharger les objets et références depuis un autre dépôt
  poule            Rapatrier et intégrer un autre dépôt ou une branche locale
  pousse           Mettre à jour les références distantes ainsi que les objets associés

'guitte help -a' et 'guitteit help -g' listent les sous-commandes disponibles et
quelques concepts. Voir 'giitte help <commande>' ou 'guitte help <concept>'
pour en lire plus à propos d'une commande spécifique ou d'un concept."""

TRANSLATIONS = {
    'copie-colle': 'clone',
    'initialisation': 'init',
    'ajout': 'add',
    'déplace': 'mv',
    'réinitialisation': 'reset',
    'enlève': 'rm',
    'couper-en-deux': 'bisect',
    'de-raisin': 'grep',
    'bûche': 'log',
    'chaud': 'show',
    'état': 'status',
    'rameau': 'branch',
    'change-arbre': 'checkout',
    'commettre': 'commit',
    'différence': 'diff',
    'fusion': 'merge',
    'refais': 'rebase',
    'graffiti': 'tag',
    'récupère': 'fetch',
    'poule': 'pull',
    'pousse': 'push',
    'cueillette-de-cerises': 'cherry-pick'
}

def usage():
    print (USAGE_STRING)
    sys.exit(1)

def main_func():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        usage()
    command = arguments[0]
    if command not in TRANSLATIONS:
        return os.system(" ".join(['git'] + arguments))
    translation = TRANSLATIONS[command]
    return os.system(" ".join(['git', translation] + arguments[1:]))

if __name__ == '__main__':
    sys.exit(main_func())
