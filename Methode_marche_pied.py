from Type_marche_pied import *


# une matrice de quantité


# creation of the instances
def graph_creation():
    print("La matrice des quantités est :")

    # Création de "S" et "C"
    proposition_quantity = [[10, 20], [0, 40]]
    empty_list = []
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    tab_s = []
    tab_c = []
    for i in range(number_row):
        tab_s.append(Sommet_pied("S" + str(i + 1), empty_list))

    for j in range(number_column):
        tab_c.append(Sommet_pied("C" + str(j + 1), empty_list))

    # Création des liaisons entre S et C
    for i in range(number_row):
        for j in range(number_column):
            nom_sommet_s = tab_s[i].nom_sommet
            nom_sommet_c = tab_c[j].nom_sommet
            if proposition_quantity[i][j] != 0:
                # Vérifie si le nom de sommet c n'est pas déjà présent dans la liste link de tab_s[i]
                if nom_sommet_c not in tab_s[i].link:
                    tab_s[i].link.append(nom_sommet_c)

                # Vérifie si le nom de sommet s n'est pas déjà présent dans la liste link de tab_c[j]
                if nom_sommet_s not in tab_c[j].link:
                    tab_c[j].link.append(nom_sommet_s)

    # affichage
    for p in range(len(tab_s)):
        print(tab_s[p].nom_sommet)
        print(tab_s[p].link)

    for m in range(len(tab_c)):
        print(tab_c[m].nom_sommet)
        print(tab_c[m].link)
    return
