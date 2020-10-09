# Projet Legal Natural Language Processing

Le but de ce projet est de faciliter la recherche juridique au travers de l'utilisation du site légifrance. Site qui héberge dans sa partie "jurisprudence" l'ensemble des décisions de justice. 

## Afin de tester l'application

Pour installer l'application, vous devez télécharger le code sous format zip. L'ouvrir dans vscode ou un autre ide. 
Ensuite vous devez installer les librairies nécessaires à l'exécution de l'appli. 
Pour cela il est fortement conseillé d'avoir au préalable installer anaconda et de créer un nouvel environnement. 

Pour télécharger jupyter anaconda: 
https://www.datacamp.com/community/tutorials/installing-anaconda-windows

Une fois jupyter anaconda installé ouvrez votre terminal et tapez la commande qui suit:

```````
conda create <myenv>
conda activate <myenv>
```````
La première commande aura pour but de créer votre nouvel environnement et la deuxième de vous placer dans ce nouvel environnement. 

Ensuite une fois que vous êtes placé dans votre nouvel environnement, pour le vérifier c'est très simple il suffit de regarder dans votre terminal vous devriez avoir quelque chose de similaire à ceci :

![Desktop Screenshot 2020 10 07 - 12 46 29 52](https://user-images.githubusercontent.com/63453012/95333643-56967f00-08ad-11eb-9900-03c7f1f60e6e.png)

La prochaine étape consiste à installer toutes les librairies pour le lancement d'application. Pour cela vous devez rentrez la commande dans le répertoire correspondant au dossier de téléchargement du code. 

``````
pip install -r requirements.txt
``````

Cela vous téléchargera toutes les librairies nécessaires, à la fin de cette procédure vous pouvez lancé l'application avec la commande 

``````
python main.py
``````
Une fois lancé dans le terminal vous aurez un lien http:// où vous devrez aller. 
Ensuite dans la première case rentrez vos mots clés pour une recherche appropriée sur légifrance. Je conseille toutefois de ne pas être trop spécifiques et de rester bien général au risque de ne pas avoir assez de données. Je préconnise ainsi deux mots clés par exemple "marchés publics critères illégales" en 4 qui donnenteux idées vous aurez une recherche qui ne prendra pas énormément de temps mais qui vous donnera une base conséquente.



Dans la deuxième case qui survient vous devez entrer le cas qui vous intéresse votre situation personnel ou celle d'une connaissance, en soit la raison qui vous a poussé à venir sur cette application. 



L'algo fera en sorte de vous dévoiler les articles, ordonnances, décrets et autres sources juridique se collant au mieux à votre contexte. 
Il cherchera aussi à vous indiquer les décisions de justices se rapprochant le plus à la problématique vous avez décrites. 



Bonne recherche. 
