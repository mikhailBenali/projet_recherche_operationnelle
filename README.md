# Consignes

Nous vous demandons de coder la résolution du problème suivant : soient n fournisseurs ayant des provisions, appelées (Pi)i∈[[1;n]] et m clients ayant fait des commandes, appelées (Cj) j∈[[1;m]].
Chaque transport unitaire d’un objet entre le fournisseur i et le client j coûte ai, j, ce qui forme la matrice A = (ai, j)(i, j)∈[[1;n]]×[[1;m]].

L’objectif est de trouver la meilleure façon de transporter les objets des fournisseurs vers les clients qui minimise le coût total du transport. C’est à dire que l’on cherche à trouver les nombres(bi, j)(i, j)∈[[1;n]]×[[1;m]] d’objet transportés depuis chaque fournisseur i vers chaque client j tels que
Σn i=1Σmj=1 ai, j ×bi, j soit minimal, sous la contrainte des provisions Σmj=1 bi, j = Pi et des commandes Σn i=1 bi, j =Cj.
Il s’agit bien évidemment du problème étudié en cours.

Dans ce cadre de ce projet, nous restreindrons l’écriture de notre programme au cas équilibré, c’està dire tel que Σn i=1 Pi = Σmj=1Cj.
Aussi, vous travaillerez avec le langage de programmation de votrechoix : C, C++, Python, Java.

## La structure globale

La structure globale de votre programme est illustrée par le pseudo-code suivant :
```
Début
    Tant que l’utilisateur décide de tester un problème de transport, faire :
        Choisir le numéro du problème à traiter
        Lire le tableau de contraintes sur fichier et le stocker en mémoire
        Créer les matrices correspondantes représentant ce tableau et l’afficher
        Demander à l’utilisateur de choisir l’algorithme pour fixer la proposition initiale et l’exécuter.
        Afficher les éléments précédemment évoqués lors de l’exécution des deux algorithmes.
        Dérouler la méthode du marche-pied avec potentiel en affichant à chaque itération :
            ⋆ Affichage de la proposition de transport, ainsi que son coût de transport total.
            ⋆ Test pour savoir si la proposition de transport est dégénérée.
            ⋆ Modifications du graphe de transport pour obtenir un arbre, dans les cas cyclique ou
            non connexe.
            ⋆ Calcul et affichage des potentiels.
            ⋆ Affichage des tables : coûts potentiels et coûts marginaux.
                ⋆ Si elle n’est pas optimale :
                Affichage de l’arête à ajouter.
                Maximisation du transport sur le cycle formé et une nouvelle itération.
                ⋆ Sinon sortir de la boucle
                ⋆ Fin si
        Afficher la proposition de transport optimale, ainsi que son coût.
        Proposer à l’utilisateur de changer de problème de transport
    fin Tant que
Fin
```

## Améliorations possibles

Une fois l’algorithme suffisamment testé, nous vous proposons les améliorations suivantes :

1. Lors du "Modifications du graphe de transport pour obtenir un arbre, dans les cas cyclique ou
non connexe", il faudra d’abord détecter si le graphe présente un cycle. Après avoir maximisé
sur ce cycle la proposition de transport, il se peut qu’il reste d’autres cycles. Il faudra alors
relancer, de manière répétée, les fonctions de "Détection de cycle", puis "Maximisation sur le
cycle" jusqu’à l’obtention d’une proposition acyclique. Ce n’est qu’après que l’on effectuera
le test de connexité où l’on complétera, au besoin, le graphe avec des arêtes classées selon des
coûts croissants jusqu’à l’obtention d’une proposition connexe et acyclique.
2. Lors de l’exécution de la fonction "Maximiser le transport sur un cycle", il se peut que δ = 0,
c’est à dire que cela n’induit pas de modification sur le cycle. Vous pouvez alors détecter ce
cas particulier. On agira ainsi : on conservera l’arête améliorante détectée avec la table des
coûts marginaux (s’il s’agit de la boucle générale) et on enlèvera l’entièreté des dernières arêtes
ajoutées lors du dernier test de connexité, à la même itération. La fonction "Modification du
graphe s’il est non connexe" qui suivra proposera alors un ensemble différent d’arêtes.

## Les traces d’exécution

Les traces d’exécution pour les 12 graphes fournis en annexes sont demandés dans le rendu. On
appelle trace d’exécution ce qui est affiché par la console. Elles ne pourront pas être remplacées par
des copies d’écran.
Il faudra exécuter avec votre programme les 12 problèmes dans les deux cas : proposition initiale
Nord-Ouest NO puis Balas-Hammer BH. Puis on affichera le déroulé du marche-pied avec potentiel
avec l’entièreté des tableaux et des informations précédemment demandées.
Les fichiers seront stockés de la façon suivante :
⋆ Groupe B - Equipe 4 - Problème 5 - Nord-Ouest : "B4-trace5-no.txt"
⋆ Groupe D - Equipe 2 - Problème 12 - Balas-Hammer : "D2-trace12-bh.txt"