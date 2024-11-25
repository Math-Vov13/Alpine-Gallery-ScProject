# API
Bienvenue dans le README de l'API</br>
développé par Mathéo VOVARD</br>

Cette API est actuellement hébergée sur un serveur Heroku: vous n'aurez donc pas besoin de la lancer manuellement, ni d'installer les dépendances python.</br>
Mais si vous voulez tout de même voir son fonctionnement en local, vous pouvez suivre la suite des instructions</br>

Vous avez le schéma de l'API [ici](/api/API.md)

## Quick Start
1. Création de l'environnement venv
```sh
python -m venv .venv
```

2. Activer l'environnement
```sh
.venv\Scripts\activate.bat  # ON WINDOWS

source .venv/bin/activate # ON LINUX/MAC
```

3. Installer les dépendances (dans `AlpineEFREI-TeamZETA/`)
```sh
pip install -r requirements.txt
```

- ou si vous utilisez [Poetry](https://python-poetry.org/docs/)
```sh
poetry install
```

4. Lancer le serveur en localhost. <br>
Exécutez les deux lignes suivantes :
```sh
cd ./src
uvicorn main:app --reload # Soyez certains
```

ou avec poetry
```sh
cd .\src
poetry run uvicorn main:app --reload
```
/!\ Si "uvicorn n'est pas une commande", s'assurer de bien exécuter `pip install -r requirements.txt` dans le fichier racine (AlpineEFREI-TeamZeta/)

## Deployment
Heroku / Firebase

## License
Mathéo Vovard