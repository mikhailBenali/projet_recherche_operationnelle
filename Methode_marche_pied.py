from Type_marche_pied import *


# une matrice de quantité


# creation of the instances
def graph_creation(proposition_quantity):
    # print("La matrice des quantités est :")

    # Création de "S" et "C"
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    tab_s = []
    tab_c = []

    for i in range(number_row):
        tab_s.append(Sommet_pied("S" + str(i + 1), i))
        tab_s[i].id_sommet = i

    for j in range(number_column):
        tab_c.append(Sommet_pied("C" + str(j + 1), j+number_row))
        tab_c[j].id_sommet = len(tab_s)+j

    # Création des liaisons entre S et C
    for i in range(number_row):
        for j in range(number_column):
            nom_sommet_s = tab_s[i].nom_sommet
            nom_sommet_c = tab_c[j].nom_sommet
            id_sommet_s = tab_s[i].id_sommet
            id_sommet_c = tab_c[j].id_sommet
            if proposition_quantity[i][j] != 0:
                # Vérifie si le nom de sommet c n'est pas déjà présent dans la liste link de tab_s[i]
                if nom_sommet_c not in tab_s[i].link:
                    tab_s[i].link.append(nom_sommet_c)
                    if id_sommet_c not in tab_s[i].link_id:
                        tab_s[i].link_id.append(id_sommet_c)

                # Vérifie si le nom de sommet s n'est pas déjà présent dans la liste link de tab_c[j]
                if nom_sommet_s not in tab_c[j].link:
                    tab_c[j].link.append(nom_sommet_s)
                    if id_sommet_s not in tab_c[j].link_id:
                        tab_c[j].link_id.append(id_sommet_s)
    tab_sommet_id = tab_s + tab_c
    # affichage
    for p in range(len(tab_s)):
        print(tab_s[p].nom_sommet)
        print(tab_s[p].link)

    for m in range(len(tab_c)):
        print(tab_c[m].nom_sommet)
        print(tab_c[m].link)

    print("Tableau groupé")
    for o in range(len(tab_sommet_id)):
        print(tab_sommet_id[o].id_sommet)
        print(tab_sommet_id[o].link_id)
    return tab_c, tab_s, tab_sommet_id


"""def calcul_nombre_sommet():
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])"""


def verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id):
    # Nous vérifions si graphe contient moins de |V | − 1 arête (|V | étant le nombre de sommets).
    # Calcul nombre de sommets
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    nombre_sommet = number_row + number_column

    # Calcul nombre d'arêtes
    nombre_arêtes = 0
    for i in range(number_row):
        for j in range(number_column):
            if proposition_quantity[i][j] != 0:
                nombre_arêtes += 1

    # Si oui, il est dégénéré
    if nombre_arêtes < nombre_sommet - 1:
        return True

    # Nous vérifions s'il y a un cycle
    # Pour ça on parcourt le graphe en partant de S1
    nombre_de_sommets_a_parcourir = nombre_sommet - 1
    sommet_origine = Sommet_pied("S0", 1000000)
    sommet_actuel = tab_sommet_id[0]
    sommet_actuel.parent = sommet_origine
    sommets_supr_nom = []
    trajet_envisageable = []
    # Si le premier sommet n'est relié à rien alors, il est dégénéré
    if sommet_actuel.link is None:
        print("SOMMET PAS RELIE")
        return True

    # On commence à parcourir le sommet actuel pour savoir où aller
    while nombre_de_sommets_a_parcourir+1 > 0:
        print("On est dans le sommet avant itération :", sommet_actuel.id_sommet)

        print(nombre_de_sommets_a_parcourir)
        # On veut voir où on peut aller
        print("On commence a regarder les enfants. Le sommet", sommet_actuel.id_sommet, "ou", sommet_actuel.nom_sommet, "a", len(sommet_actuel.link_id), "enfants")
        print("Le parent du sommet est", sommet_actuel.parent.nom_sommet)
        for i in range(len(sommet_actuel.link_id)):
            print("Un enfant est", sommet_actuel.link_id[i])
            # On regarde un sommet dans la liste des sommets
            # On ne va pas dans le sommet prédécesseur
            # ajout dans trajet envisageable d'un element qui n'est pas le prédécesseur
            index = sommet_actuel.link_id[i]
            prochain_sommet_nom = tab_sommet_id[index]
            prochain_sommet_nom.parent = sommet_actuel
            print("THE parent à la création", prochain_sommet_nom.parent.id_sommet)
            print("Prochain sommet dans i: ", prochain_sommet_nom.id_sommet)
            # On check si le prochain sommet n'est pas le prédécesseur (parent)

            if prochain_sommet_nom != sommet_actuel.parent:
                # Si le prochain sommet n'est pas un parent, mais est un sommet où on est passé
                if prochain_sommet_nom in sommets_supr_nom:
                    print("Cycle")
                    return True
                else:
                    trajet_envisageable.append(prochain_sommet_nom.id_sommet)
                    print(prochain_sommet_nom.id_sommet, "ajouté")
        print("Sommets envisageable :", trajet_envisageable)
        print("On a fini d'ajouter les sommets")

        # Maintenant qu'on a ajouté depuis notre somme ceux à quoi il est relié
        # On veut changer le sommet actuel parmi ceux disponibles, changer les sommets sup et set le parent
        if trajet_envisageable:
            # for i in range(len(tab_sommet_id)):
            print(prochain_sommet_nom.id_sommet)
            print(tab_sommet_id[i].parent)
            # On fait effectivement le trajet
            print("Sommet actuel avant voyage mais après les calculs pour le prochain", sommet_actuel.id_sommet)
            # while trajet_envisageable:
            sommets_supr_nom.append(sommet_actuel)
            # On change le sommet precedent
            # tab_sommet_id[0].parent = sommet_actuel
            # On va au premier trajet de la liste
            # print("len", len(tab_sommet_id))
            # print("le big tableau",trajet_envisageable)
            print("NB a parcourir: ", nombre_de_sommets_a_parcourir)
            # On prend le sommet précédent
            sommet_precedent = tab_sommet_id[sommet_actuel.id_sommet]
            # On change le sommet actuel
            sommet_actuel = tab_sommet_id[trajet_envisageable[0]]
            # On setup le parent du sommet actuel
            # sommet_actuel.parent = sommet_precedent
            print("Le sommet actuel est :", sommet_actuel.id_sommet, "Le sommet précédent est :", sommet_precedent.id_sommet)
            print("Le parent est de", sommet_actuel.id_sommet, "est", sommet_actuel.parent.id_sommet)
            # On supprime le premier trajet de la liste
            trajet_envisageable.pop(0)

        # Vérifie si un des prochains n'est pas un déjà parcouru, car sinon cycle
        # On parcourt tous les liens du sommet actuel et tous les sommets supr
        """for i in range(len(sommet_actuel.link)):
            for j in range(len(sommets_supr_nom)):
                # Si c'est un truc qu'on a déjà parcouru et que ce n'est pas le prédécesseur
                if (sommet_actuel.link[i] == sommets_supr_nom[j]) & (sommet_actuel.link != sommet_precedent_nom):
                    return True"""
        nombre_de_sommets_a_parcourir = nombre_de_sommets_a_parcourir - 1
        print("SOMMETS SUPR", sommets_supr_nom)

        print("BIG FIN DE L'ITERATION")
        # si la liste des destinations n'est pas vide, alors cycle

    return False



# supprimer du tableau tous_les_sommets ceux où on est déjà passé
# tous_les_sommets.pop(tous_les_sommets.index(sommet_actuel))

#print("Sommet parcourus : ", sommets_parcourus)
#print("Sommet actuel : ", sommet_actuel)