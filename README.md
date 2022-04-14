# OC-P7-GrandPy_Bot

version finale au tag v1.0

## introduction
 projet d'études mêlant requêtes d'API, flask, et TDD
## cahier des charges
### Fonctionnalités
* Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
* Vous utiliserez l'API de Google Maps et celle de Media Wiki.
* Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !
### Parcours utilisateur

L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :

* header : logo et phrase d'accroche
* zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.
* footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez

L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.
Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.
GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"

## contraintes
* Interface responsive
* Test Driven Development
* Code intégralement écrit en anglais : fonctions, variables, commentaires, ...
* Utilisation d'AJAX pour l'envoi des questions et l'affichage des réponses (les questions et réponses sont en une seule langue au choix, anglais ou français)
* Tests utilisant des mocks pour les API
* hébergement sur Heroku

# OC-P11-Enhance a former project

version finale au tag v1.1

nouvelle fonctionnalité: ajout d'une fenêtre modale de statistiques contenant le nombre de requêtes pointant vers chaque région française