# API ![alt text](https://cdn.discordapp.com/attachments/1291488602362089503/1310751901687611462/imageedit_4_7508579979.png?ex=67465c55&is=67450ad5&hm=b19415aa4665c76ced2cc3e0057b4f0849ec883f9d967c148d39d900316e23f6&)
Bienvenue dans le README de l'API</br>
développé par Mathéo VOVARD</br>

Cette API est actuellement hébergée sur un serveur Heroku: vous n'aurez donc pas besoin de la lancer manuellement, ni d'installer les dépendances python.</br>
Mais si vous voulez tout de même voir son fonctionnement en local, vous pouvez suivre la suite des instructions</br>

Vous avez le schéma de l'API [ici](/api/API.md)

# INSTRUCTIONS

## Quick Start
1. Création de l'environnement venv
```sh
python -m venv .venv
```
2. Installer les dépendances (dans `AlpineEFREI-TeamZETA/`)
```sh
pip install -r requirements.txt
```

- ou si vous utilisez [Poetry](https://python-poetry.org/docs/)
```sh
poetry install
```

3. Lancer le serveur en localhost. <br>
Exécutez les deux lignes suivantes :
```sh
cd ./src
uvicorn main:app --reload # Soyez certain que vous exécutez cette ligne dans ./src !
```

ou avec poetry
```sh
cd .\src
poetry run uvicorn main:app --reload
```
## **ATTENTION** ![alt text](https://cdn.discordapp.com/attachments/1291488602362089503/1310720174021935104/image.png?ex=67463ec9&is=6744ed49&hm=be6cbd10e92be9ce3a0d7094c5d76f9301d96f3d4b08c32699ea7b764f9360c0&)

![alt text](https://cdn.discordapp.com/attachments/1291488602362089503/1310719235571318885/image.png?ex=67463de9&is=6744ec69&hm=bc9f4f00867700be78ec0d3093039cccdcc8e5423cd79b310c3517da19b3af4b&) // Si votre terminal affiche `uvicorn n'est pas une commande`, s'assurer de bien exécuter `pip install -r requirements.txt` dans le fichier racine AlpineEFREI-TeamZeta/`

## Deploiement 
Heroku / Firebase -- 

## License
Mathéo VOVARD
