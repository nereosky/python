
build : Cette commande permet la création d'une image à partir d'un Dockerfile et d'un "contexte". Le contexte représente l'ensemble des fichiers se troiuvant dans le répertoie ou à l'adresse indiquée.

run : Cette commande permet de définir les ressources utilisées par le conteneur. La commande doit sépcifier une IMAGE.

exec : Cette commande permet d'executer une commande dans le conteneur en cours d'utilisation. Une commande lancée de cette manière n'est pas redémarrée si le conteneur est relancé.

Les containers: Un conteneur est un processus isolé des autres processus de la machine hôte.

Les images: Quand un conteneur est actif, il utilise un système isolé. Ce système est fourni par l'image du conteneur. L'image doit contenir tout ce qui est nécessaire au fonctionnement de l'application ainsi que différents configuratuions pour le conteneur tels que les variables d'environnement et différentes métadonnées.