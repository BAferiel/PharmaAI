![Django Logo](https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg)
# Online Health Prediction using Django

## 🏥 Introduction

Ce projet propose une **plateforme de prédiction de santé en ligne** basée sur **Django**. Il utilise des modèles d'apprentissage automatique pour fournir des prédictions concernant diverses conditions de santé, notamment :

- Troubles mentaux  
- Syndrome des ovaires polykystiques (PCOS)  
- Obésité  

Les prédictions sont générées à partir de **modèles entraînés sur des datasets provenant de Kaggle**. En plus des analyses prédictives, la plateforme permet aux utilisateurs de télécharger leurs **rapports de santé** en ligne et de planifier des **rendez-vous avec des professionnels de santé**.  

---

## ✨ Fonctionnalités Principales

1. **Prédictions de santé** : Utilisation de modèles ML pour fournir des prévisions précises sur plusieurs conditions de santé.  
2. **Téléchargement de rapport** : Les utilisateurs peuvent télécharger leurs rapports personnalisés.  
3. **Prise de rendez-vous** : Les utilisateurs peuvent fournir leurs coordonnées et envoyer un message pour planifier un rendez-vous.  
4. **Gestion des rendez-vous** : Les professionnels de santé peuvent s'enregistrer et gérer les rendez-vous.  
5. **Communication médecin-patient** : Les docteurs peuvent voir et accepter les demandes de rendez-vous en ligne.  

---

## 🛠️ Technologies Utilisées

- **Django** : Framework backend pour le développement web.
- **HTML / CSS / Bootstrap** : Interface utilisateur front-end.
- **Python** : Langage de programmation utilisé pour l’entraînement des modèles et la gestion du backend.
- **Scikit-learn / TensorFlow** : Outils pour l’entraînement des modèles de machine learning.
- **SQLite** : Base de données utilisée par défaut avec Django.
- **Kaggle Datasets** : Sources de données pour entraîner les modèles prédictifs.

---

## 📦 Installation et Configuration

### 1. Prérequis
- **Python 3.x** installé
- **pip** (Python package installer)
- **Git**

### 2. Cloner le Repository
```bash
git clone https://github.com/BAferiel/PharmaAI.git
cd PharmaAI
### 3. Créer un Environnement Virtuel
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
### 4. Installer les Dépendances
pip install -r requirements.txt
### 5. Appliquer les Migrations
python manage.py migrate
### 6. Lancer le Serveur de Développement
python manage.py runserver
L’application sera accessible à l’adresse suivante : http://127.0.0.1:8000
🧠 Modèles de Machine Learning
Les modèles sont entraînés sur des datasets Kaggle et intégrés dans l’application pour fournir des prédictions en temps réel. Voici les principaux types de modèles utilisés :

Régression logistique pour la prédiction de l'obésité.
Random Forest pour les troubles mentaux.
SVM (Support Vector Machine) pour le syndrome des ovaires polykystiques (PCOS).
