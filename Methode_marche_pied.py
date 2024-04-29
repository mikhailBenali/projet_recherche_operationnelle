from Type_marche_pied import *


# une matrice de quantité


# creation of the instances
def graph_creation(proposition_quantity):
    print("La matrice des quantités est :")

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
                    if id_sommet_s not in tab_c[i].link_id:
                        tab_c[i].link_id.append(id_sommet_s)

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


def calcul_nombre_sommet():
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])


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
    nombre_de_sommets_a_parcourir = nombre_sommet
    sommets_parcourus = []
    sommet_actuel = tab_s[0]
    tous_les_sommets = tab_s + tab_c
    sommets_supr_nom = []
    sommet_precedent_nom = None
    trajet_envisageable = []
    # Si le premier sommet n'est relié à rien alors, il est dégénéré
    if sommet_actuel.link is None:
        return True
    while nombre_de_sommets_a_parcourir > 0:
        # Vérifie si un des prochains n'est pas un déjà parcouru, car sinon cycle
        # On parcourt tous les liens du sommet actuel et tous les sommets supr
        for i in range(len(sommet_actuel.link)):
            for j in range(len(sommets_supr_nom)):
                # Si c'est un truc qu'on a déjà parcouru et que ce n'est pas le prédécesseur
                if sommet_actuel.link[i] == sommets_supr_nom[j] & sommet_actuel.link != sommet_precedent_nom:
                    return True
        # On veut voir où on peut aller
        for i in range(len(sommet_actuel.link)):
            # On regarde un sommet dans la liste des sommets
            # On ne va pas dans le sommet prédécesseur
            if sommet_actuel.link[i] != sommet_precedent_nom:
                # ajout dans trajet envisageable d'un element qui n'est pas le prédécesseur

                # GROS PB CA NE COPIE QUE LE NOM DU SOMMET, PAS LE SOMMET LUI MEME
                prochain_sommet_nom = sommet_actuel.link[i]
                trajet_envisageable.append()
        # On fait effectivement le trajet
        while trajet_envisageable is not None:
            sommets_supr_nom = sommet_actuel.nom_sommet
            # On change le sommet precedent
            sommet_precedent_nom = sommet_actuel.nom_sommet
            # On va au premier trajet de la liste
            sommet_actuel = trajet_envisageable[0]
            # On supprime le premier trajet de la liste
            trajet_envisageable.pop(0)



    return False



# supprimer du tableau tous_les_sommets ceux où on est déjà passé
# tous_les_sommets.pop(tous_les_sommets.index(sommet_actuel))

#print("Sommet parcourus : ", sommets_parcourus)
#print("Sommet actuel : ", sommet_actuel)