# Backdoor Project

## Description

Ce projet implémente une backdoor simple en utilisant Python. Il se compose de deux fichiers principaux : `client.py` et `server.py`. Le fichier `client.py` agit comme le client (ou l'agent malveillant) qui s'exécute sur la machine cible, tandis que `server.py` agit comme le serveur (ou le contrôleur) qui reçoit les connexions et les commandes du client.

### AVERTISSEMENT

Ce projet est uniquement à des fins éducatives et de recherche en cybersécurité. L'utilisation non autorisée de ce logiciel pour accéder à des systèmes informatiques sans la permission explicite du propriétaire est illégale et éthiquement inacceptable. Les auteurs déclinent toute responsabilité pour les actions réalisées avec ce code.

## Fonctionnalités

- **client.py** : Se connecte au serveur, attend les commandes, et exécute les instructions reçues.
- **server.py** : Accepte les connexions des clients, envoie des commandes aux clients connectés, et reçoit les résultats des commandes exécutées.

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-utilisateur/backdoor-project.git
cd backdoor-project
2. Installez les dépendances nécessaires (le cas échéant) :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Serveur

1. Lancez le serveur sur votre machine de contrôle :

    ```bash
    python server.py
    ```

2. Le serveur écoutera les connexions entrantes sur un port spécifié (par défaut 4444).

### Client

1. Exécutez le client sur la machine cible :

    ```bash
    python client.py
    ```

2. Le client se connectera au serveur spécifié dans le code et attendra les commandes.

### Exemple

Pour lancer le serveur :

```bash
python server.py --host 0.0.0.0 --port 4444
```
Pour lancer le client :

```bash
python client.py --host 0.0.0.0 --port 4444
```
