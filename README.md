# Consignes

Nous vous demandons de coder la résolution du problème suivant : soient n fournisseurs ayant des provisions, appelées (Pi)i∈[[1;n]] et m clients ayant fait des commandes, appelées (Cj) j∈[[1;m]]. 
Chaque transport unitaire d’un objet entre le fournisseur i et le client j coûte ai, j, ce qui forme la matrice A = (ai, j)(i, j)∈[[1;n]]×[[1;m]].

L’objectif est de trouver la meilleure façon de transporter les objets des fournisseurs vers les clients qui minimise le coût total du transport. C’est à dire que l’on cherche à trouver les nombres(bi, j)(i, j)∈[[1;n]]×[[1;m]] d’objet transportés depuis chaque fournisseur i vers chaque client j tels que
Σn i=1Σmj=1 ai, j ×bi, j soit minimal, sous la contrainte des provisions Σmj=1 bi, j = Pi et des commandes Σn i=1 bi, j =Cj.
Il s’agit bien évidemment du problème étudié en cours.

Dans ce cadre de ce projet, nous restreindrons l’écriture de notre programme au cas équilibré, c’està dire tel que Σn i=1 Pi = Σmj=1Cj.
Aussi, vous travaillerez avec le langage de programmation de votrechoix : C, C++, Python, Java.
