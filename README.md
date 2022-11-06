# Stéganographie

> La stéganographie est un domaine où l'on cherche à dissimuler discrètement de l'information dans un media de couverture (typiquement un signal de type texte, son, image, vidéo, etc.).
##### Le principe est le suivant : deux images sont fusionnées de telle façon que chaque pixel de l'image finale est définie sur 8 bits. Les bits de point fort sont les bits de point fort de la première image tandis que les bits de point faible sont les bits de point fort de la seconde image. Ainsi, la deuxième image est dissimulée dans la première.
##### Minimum Viable Product :
- pouvoir créer une image à partir de deux images en dissimulant la deuxième.
- être capable de séparer les deux images qui constituent l'image finale.
##### Ameliorations futures:
- utiliser des découpages différents (3 bits de la première image et 5 de la deuxième, 5/3, 6/2).
- utiliser des images de différentes tailles.
- interface graphique ???
##### 2 fonctions:
- cacher() qui récupère les codes r,v,b de chaque pixel des deux images (image_front et image_back) et qui les convertie en binaire pour les redistribuer et creer les pixels d'une troisième image (img_coder).
- decoder() qui part de l'image créée par cacher() et récupère les bits de points forts des deux images cachées.
##### Bibliothèques importées:
- PIL
