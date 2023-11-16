<p align="center">
  <a href="https://github.com/Rayan-El-Manssouri/Majax#readme">
    <img src="./assets/detailled dark.svg" alt="Majax logo" style="max-width: 30%;" >
  </a>
</p>

<h3 align="center">Majax API</h3>
<p align="center"><i>Connectivité fluide, réponses rapides : notre serveur API redéfinit l'efficacité en ligne!</i></p>

---

Majax est un protocole de communication utilisé dans notre messagerie instantanée Mercure. Elle permet simplement à l'interface de gérer les communications avec le serveur et ainsi les fonctionnalités de la messagerie.

# Table de matieres

- ``Installation du project``
- ``Liste des routes disponibles``
- ``Structure du projet``
- ``issues``
- ``Contribution``

# Installation du projet

Install Dependencies :

````white
pip install -m requirements.txt
````

## Dependencies :
- flask
- flask_session
- flask_cors
- flask_jwt_extended

# Liste des routes disponibles :

- POST ``/register`` : Cette route nécessite la clé publique (public_key) dans le headers ``Authorization`` spécifiée dans le fichier config.ini.
- POST ``/login`` : Cette route demande un body : { email, password } elle créa un jwt signier par une clé RSA grâce aux private_key / public_key in config.ini .
- POST ``/logout`` : Cette route demande un body {email} et un headers : {``Authorization``} elle nécessite une clé jwt génerer par le serveur.
- POST ``/Fetch_Pseudo`` : Cette route demande un body {user_email} et un headers {``Authorization``} elle nécessite une clé jwt génerer par le serveur.
- POST ``/CheckLogin`` : Cette route demande un body {email} et un headers {``Authorization``} elle nécessite une clé jwt génerer par le serveur.

# Structure du projet

- ``/assets`` Dossier d'image
- ``/Color`` Une class color pour l'affichiage de console
- ``/Database`` Structure de la bdd
- ``/Utils`` quelque class autre pour le code python
- ``config.ini`` Fichier principal de configuration

#  issues

Lorsqu'il y a un bug identifié ou une suggestion, veuillez les signaler dans les issues de GitHub.

# Security

Afin de s'assuer en therme de sécuriter les clé jwt sont eux même signer via une clé RSA en RS256.

# Contribution

- OWNER ``prorayanelmanssouri@gmail.com``