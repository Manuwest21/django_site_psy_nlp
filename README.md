# Projet Django - Suivi des Patients

Ce projet Django est conçu pour vous aider à suivre les informations des patients, y compris leurs noms, dates et prédictions. Il permet également de filtrer et d'afficher la répartition des valeurs prédites sur une période donnée.
Configuration requise

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

    Python (version 3.6 ou supérieure)
    Django (version 3.0 ou supérieure)

# Installation

    Clonez ce dépôt sur votre machine locale : git clone git@github.com:Manuwest21/django_site_psy_nlp.git

    Accédez au répertoire du projet : cd spsy

Installez les dépendances requises :

    pip install -r requirements.txt

Effectuez les migrations de la base de données :

    python manage.py migrate

Lancez le serveur de développement :

    python manage.py runserver

    Le site sera accessible à l'adresse http://localhost:8000/.

# Utilisation

Vue période

    La vue "période" vous permet de filtrer et d'afficher la répartition des valeurs prédites pour une période donnée. Vous pouvez sélectionner le mois de début et le mois de fin dans les listes déroulantes correspondantes. De plus, vous pouvez filtrer les résultats en entrant le prénom et/ou le nom du patient dans les champs de recherche correspondants.
    Modèles

Le projet utilise un modèle appelé Le_patient_date pour stocker les informations des patients. Le modèle comprend les champs suivants :

    patient_lastname: le nom de famille du patient (champ CharField).
    patient_name: le prénom du patient (champ CharField).
    date: la date associée au patient (champ DateField).
    predicted: la valeur prédite pour le patient (champ CharField).
    confidence: le niveau de confiance associé à la prédiction (champ FloatField).

# Docker-compose

    Dans ce projet la DB utilisé est PostgreSQL. Vous trouverez un fichier docker-compose qui permet de déployer une DB en local. Vous trouverez également un fichier csv pour remplir la DB et tester les fonctionalités du site.

Licence

    Ce projet est sous licence MIT.