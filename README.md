Binôme: KLIEBER Nathan MARTINGOULET Ulric 

choix technique:

1 Choix du langage : Python
Python est simple, lisible et idéal pour un projet académique ou un prototype CLI.
Permet d’utiliser facilement :
Les dataclasses pour représenter les entités (Student).
Les modules standard (csv, json, sys) pour gérer la CLI et l’export.
Large écosystème si besoin de fonctionnalités avancées (bases de données, frameworks).

2 Gestion de versions : Git

Git permet de :
Travailler en branches (main, feature/...) pour séparer les développements.
Fusionner les branches et gérer les conflits de manière sécurisée.
Travailler en collaboration sur un dépôt distant (origin) sans perdre d’historique.
Le workflow utilisé (feature branches, pull, merge, push) est standard dans l’industrie et facilite la collaboration.

3 Architecture CLI + Service

Séparation des responsabilités :
Main.py → interface utilisateur (CLI)
StudentService → logique métier (ajout, suppression, export)
Avantage :
Code plus modulaire, réutilisable et testable.
Ajout de nouvelles fonctionnalités (ex: export supplémentaire) sans modifier la CLI de façon massive.

4 Gestion des formats d’export

Choix d’utiliser CSV et JSON :
JSON → facile à lire, compatible avec d’autres systèmes.
CSV → simple pour traitement tabulaire (Excel, Google Sheets).
Permet de répondre à différents besoins d’utilisateurs et de démontrer flexibilité technique.

5 Choix Git et workflow collaboratif
Utilisation des feature branches : chaque fonctionnalité est développée sur une branche séparée.
Permet :
Tester les fonctionnalités isolément.
Intégrer dans main seulement quand elles sont stables.
Pousser sur le dépôt distant pour garder une sauvegarde et partage avec l’équipe.

Gestion des branches

git branch	Liste les branches locales
git branch -d nom_branche	Supprime une branche locale (si fusionnée)
git branch -D nom_branche	Supprime une branche locale forcée
git branch -m ancien_nom nouveau_nom	Renommer une branche
git switch nom_branche	Activer/se placer sur une branche existante
git switch -c nom_branche	Créer et activer une nouvelle branche
git checkout nom_branche	Ancienne méthode pour activer une branche
git checkout -b nom_branche	Créer et activer une branche (ancienne méthode)
git merge feature/...	Fusionner une branche dans la branche courante
git rebase main	Repositionner l’historique d’une branche sur une autre

Gestion du dépôt distant (remote)
Commande	Rôle
git remote -v	Vérifie les dépôts distants (origin)
git remote add nom URL	Ajouter un dépôt distant
git push origin nom_branche	Pousser les commits locaux vers le dépôt distant
git push -u origin nom_branche	Pousser et configurer la branche upstream
git push origin --delete nom_branche	Supprimer une branche distante

Récupération et synchronisation
Commande	Rôle
git pull	Récupérer les commits distants et fusionner dans la branche locale
git pull --rebase	Récupérer et rebaser vos commits locaux sur les commits distants
git fetch	Récupérer les commits distants sans fusionner

Gestion des fichiers et commits
Commande	Rôle
git add fichier	Ajouter un fichier à l’index pour le prochain commit
git commit -m "message"	Créer un commit avec un message
git rm fichier	Supprimer un fichier suivi par Git
git rm --cached fichier	Supprimer un fichier du suivi Git mais le garder localement
git status	Vérifier l’état des fichiers (modifiés, ajoutés, non suivis)
git log --oneline