les commandes dans le dockerfile:

la commande FROM:
la fonction pour appeler une image qui servira de base a l'application
la commande run:
(on peut en faire plusieurs) commande pour créer l'application.
la commande copy:
permet de copier vers la position indiquée
la commande expose:
c'est pour spécifier le port qu'on va utiliser
la commande cmd:
commande que l'on veut executer dans le conteneur

les commandes dans le terminal/ cmd
docker build permet de faire une image depuis le conteneur indiqué
docker run permet d'instancier une image
docker exec pour lancer une commande sur le conteneur
docker ps pour savoir quels sont les conteneurs qui tournent
docker images pour afficher les images qu'on a recup

exemple :
docker build -t [nom du fichier]:01 .
docker run -d -p 5000:5000 [nom du fichier]:01
docker exec -it [le retour du run] /bin/bash
docker logs [id renvoyé par le build]