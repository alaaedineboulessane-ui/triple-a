# 🖥️ Challenge Triple A – Dashboard de Monitoring

## 📌 Description
Ce projet génère automatiquement une page HTML contenant un **dashboard complet d’informations système** :  
- Nom de la machine  
- OS et version  
- Uptime  
- Nombre d’utilisateurs connectés  
- Informations CPU  
- Utilisation de la RAM  
- Adresse IP locale  
- Top 3 des processus les plus gourmands  
- Statistiques sur les types de fichiers dans un dossier donné  

Le script utilise Python et la librairie **psutil** pour récupérer des informations système et les injecter dans un fichier HTML via un template.

## 📦 Prérequis
Avant d’exécuter le programme, vous devez installer :

- **Python 3.8+**
- Le module Python :
  - `psutil`

Vous devez également avoir dans le même dossier :
- `template.html` (modèle HTML utilisé pour générer la page finale)
- `template.css` (feuille de style si utilisée)

## ⚙️ Installation

Clonez ou téléchargez le projet puis installez les dépendances requises.

### Commandes pour installer les dépendances


Aucune autre dépendance externe n'est nécessaire.

## 🚀 Utilisation

### 1. Lancer le script Python

Dans un terminal ouvert dans le dossier du projet :


> Le programme lit le fichier `template.html`, remplace les variables, puis génère un fichier **result.html** contenant toutes les informations système.

### 2. Ouvrir la page HTML générée

Une fois le script exécuté, ouvrez simplement le fichier :


dans n’importe quel navigateur web (Chrome, Firefox, Edge, etc.).

## 🔧 Fonctionnalités

### ✔ Informations système
- Nom de la machine  
- Système d’exploitation + version  
- Uptime (en minutes)  
- Nombre d’utilisateurs  

### ✔ Analyse CPU
- Nombre de cœurs  
- Fréquence actuelle  
- % d'utilisation CPU  
- Top 3 des processus les plus gourmands  

### ✔ Analyse mémoire
- RAM totale  
- RAM utilisée  
- Pourcentage d'utilisation  

### ✔ Réseau
- Adresse IP principale  

### ✔ Analyse de fichiers
Analyse d’un dossier (exemple : `Documents/`) et calcule :  
- Nombre de fichiers `.txt`, `.pdf`, `.jpg`, `.webp`, `.ahk`, `.url`, `.docx`  
- Nombre de sous-dossiers  
- Pourcentage de chaque type

### ✔ Génération automatique d'une page HTML
Les données sont injectées dans un template afin de produire un dashboard visuel.

## 🖼️ Captures d'écran



## ⚠️ Difficultés rencontrées
Quelques points ont pu poser problème :

- Gestion des processus avec `psutil` (certaines permissions provoquent des erreurs → nécessité de gérer `AccessDenied` et `NoSuchProcess`).
- Nécessité d’attendre une seconde pour obtenir une valeur CPU fiable pour chaque processus.
- Manipulation des chemins Windows dans la fonction d’analyse des fichiers.
- Encodage UTF-8 pour lire et écrire correctement le template HTML.

## 🚀 Améliorations possibles

- Ajouter un **serveur Flask** pour afficher dynamiquement les données sans générer un fichier HTML statique.
- Ajouter des **graphes** (CPU, RAM, stockage) avec Chart.js.
- Faire un design plus moderne du dashboard.
- Rendre les chemins et options configurables via un fichier `.env`.
- Ajouter un mode sombre / clair.
- Ajouter une API pour exposer les données système.

## 👤 Auteur
**Nom :Boulessane Alaaedine, Baili Anas**
**Projet :** Challenge Triple A  
**Année :** 2025

