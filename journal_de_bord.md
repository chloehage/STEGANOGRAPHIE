## 25/10
- création d'un fonction cacher() qui récupère chaque pixel des deux images à fusionner et forme les pixels de l'image finale, les 4 premiers bits étant les bits de point fort de la première image et les 4 derniers les bits de point fort de la deuxième image.

## 27/10
- création d'une fonction decoder() pour décoder l'image finale.

## 29/10
- fonction placer_pixel() pour placer les pixels créés à partir des deux images sur l'image finale. (pas utilisée au final)

## 30/10
- création du ReadMe.md et du journal_de_bord.md

## 01/11
- rectification de certaines parties du code.

## 05/11
- encore des rectifications pour que le code marche un jour :')

## 06/11
- encooore des rectifications. 
- seul problème : les bits sont dans une liste, il faut la convertir en chaine pour la convertir.

## 10/11
- convertion de la liste en chaine.

## 17/11
- ajout de 0 pour que le code RVB soit bien sur 8 bits et que la conversion en décimal marche
- on a découvert que notre fonction ne marchait pas complètement et donc on vient de découvrir à quoi notre image était censée ressembler depuis 2 semaines
- donc notre première fonction fonctionne désormais

## 24/11
- enfait on se cassait la tête à vouloir mettre les bits dans un liste alors on les a directement mis dans une chaine de caractères en ajoutant les '0' nécessaires en début de chaine.
- les images apparraissent mais sont difficiles à decrypter, elles apparaissent en très sombre
- l'image cachée quand elle est décodée bug mais maintenant l'autre est mieux :))
- code beauty = code joli
