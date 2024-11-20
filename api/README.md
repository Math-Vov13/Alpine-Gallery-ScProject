# API
Bienvenue dans le README de l'API</br>
développé par Mathéo Vovard</br>

Cette API est actuellement hébergé sur un serveur Heroku: vous n'aurez donc pas besoin de la lancer manuellement, ni d'installer les dépendances python.</br>
Mais si vous voulez tout de même voir son fonctionnement en local, vous pouvez suivre la suite des instructions</br>

Vous avez le schéma de l'API [ici](/api/API.md)

## Quick Start
1. create venv
```sh
python -m venv .venv
```
2. installer les dépendances
```sh
pip install -r requirements.txt
```

ou si vous avez [poetry](https://python-poetry.org/docs/)
```sh
poetry install
```

3. lancer le serveur en localhost
```sh
cd .\api
uvicorn main:app --reload
```

ou avec poetry
```sh
cd .\api
poetry run uvicorn main:app --reload
```


## Deployment
Heroku / Firebase

## License
Mathéo Vovard