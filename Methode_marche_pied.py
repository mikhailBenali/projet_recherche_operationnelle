from Type_marche_pied import *
import numpy as np

def graph_creation(proposition_quantity):
    print("proposition_quantity Avant :", proposition_quantity)

    proposition_quantity = proposition_quantity[:-1]
    for i in range(len(proposition_quantity)):
        proposition_quantity[i] = proposition_quantity[i][:-1]

    print("proposition_quantity Après :", proposition_quantity)
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
        tab_c.append(Sommet_pied("C" + str(j + 1), j + number_row))
        tab_c[j].id_sommet = len(tab_s) + j

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

    """for m in range(len(tab_c)):
        print(tab_c[m].nom_sommet)
        print(tab_c[m].link)"""

    """print("Tableau groupé")
    for o in range(len(tab_sommet_id)):
        print(tab_sommet_id[o].id_sommet)
        print(tab_sommet_id[o].link_id)"""
    return tab_c, tab_s, tab_sommet_id


def acyclique(proposition_quantity, tab_sommet_id):
    # Nous vérifions s'il y a un cycle
    # Pour ça on parcourt le graphe en partant de S1
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    nombre_sommet = number_row + number_column

    nombre_de_sommets_a_parcourir = nombre_sommet
    sommet_origine = Sommet_pied("S0", 1000000)
    sommet_actuel = tab_sommet_id[0]
    sommet_actuel.parent = sommet_origine
    sommets_supr_nom = []
    trajet_envisageable = []

    # Pour retrouver le cycle
    le_cycle = []
    """# Si le premier sommet n'est relié à rien alors, il est acyclique
    if sommet_actuel.link is None:
        return True"""

    # On commence à parcourir le sommet actuel pour savoir où aller
    while nombre_de_sommets_a_parcourir > 0:
        # On veut voir où on peut aller
        for i in range(len(sommet_actuel.link_id)):
            # On regarde un sommet dans la liste des sommets
            # On ne va pas dans le sommet prédécesseur
            # ajout dans trajet envisageable d'un element qui n'est pas le prédécesseur
            index = sommet_actuel.link_id[i]
            prochain_sommet_nom = tab_sommet_id[index]
            prochain_sommet_nom.parent = sommet_actuel
            # On check si le prochain sommet n'est pas le prédécesseur (parent)

            # print("Sommet actuel avant :", sommet_actuel.nom_sommet)

            if prochain_sommet_nom != sommet_actuel.parent:
                # Si le prochain sommet n'est pas un parent, mais est un sommet où on est passé
                if prochain_sommet_nom in sommets_supr_nom:
                    # IL Y A DONC UN CYCLE !
                    # On cherche le cycle
                    # On se place sur un sommet appartenant au cycle et on l'ajoute au tableau cycle
                    sommet_actuel = prochain_sommet_nom
                    le_sommet_de_base_du_cycle = sommet_actuel
                    le_cycle.append(le_sommet_de_base_du_cycle)
                    longueur_a_faire = len(sommets_supr_nom)

                    # On fait ça pour tous les sommets qu'on a parcourus pour trouver le cycle
                    while longueur_a_faire + 2 > 0:
                        # On regarde si le sommet actuel a un enfant. Sinon il ne fait pas partie du cycle
                        if len(sommet_actuel.link_id) > 1:
                            # On cherche le premier enfant uniquement (le vrai sommet pas juste son id)
                            index = sommet_actuel.link_id[0]
                            prochain_sommet_nom = tab_sommet_id[index]
                            prochain_sommet_nom.parent = sommet_actuel
                            # prochain_sommet_nom.parent_cycle = sommet_actuel
                            # Si le sommet où on se dirige est le parent, on recommence et on supprime le lien
                            if prochain_sommet_nom == sommet_actuel.parent:
                                temporaire = sommet_actuel.link_id[0]
                                sommet_actuel.link_id.pop(0)
                                index = sommet_actuel.link_id[0]
                                prochain_sommet_nom = tab_sommet_id[index]
                                prochain_sommet_nom.parent = sommet_actuel
                                # prochain_sommet_nom.parent_cycle = sommet_actuel
                                sommet_actuel.link_id.insert(0, temporaire)
                            # On vérifie si on n'a pas fait le tour du cycle, si c'est le cas, on a trouvé le cycle
                            if prochain_sommet_nom == le_sommet_de_base_du_cycle:
                                le_cycle.append(le_sommet_de_base_du_cycle)
                                return False, le_cycle
                            # On se déplace dedans
                            else:
                                sommet_actuel = tab_sommet_id[prochain_sommet_nom.id_sommet]
                                le_cycle.append(sommet_actuel)

                        # alors, il n'appartient pas au cycle
                        else:
                            # On supprime le sommet des sommets restants et du cycle
                            le_cycle.remove(sommet_actuel)
                            sommet_actuel = sommet_actuel.parent
                            sommet_actuel.link_id.pop(0)

                        longueur_a_faire -= 1
                    for p in range(len(le_cycle)):
                        print(le_cycle[p].nom_sommet)
                    return False, le_cycle

                else:
                    trajet_envisageable.append(prochain_sommet_nom.id_sommet)

        # Maintenant qu'on a ajouté depuis notre somme ceux à quoi il est relié
        # On veut changer le sommet actuel parmi ceux disponibles, changer les sommets sup et set le parent
        if trajet_envisageable:
            # On fait effectivement le trajet
            sommets_supr_nom.append(sommet_actuel)
            # On prend le sommet précédent
            sommet_precedent = tab_sommet_id[sommet_actuel.id_sommet]
            # On change le sommet actuel
            sommet_actuel = tab_sommet_id[trajet_envisageable[0]]
            # On supprime le premier trajet de la liste
            trajet_envisageable.pop(0)

        nombre_de_sommets_a_parcourir = nombre_de_sommets_a_parcourir - 1

        # si la liste des destinations n'est pas vide, alors cycle
    return True, le_cycle


def connexe(proposition_quantity, tab_sommet_id):
    compteur_sommets = 0
    all_non_connex = []
    empty_tab = []

    reel_quantity = proposition_quantity
    for i in range(len(tab_sommet_id)):
        sommet_actuel = tab_sommet_id[i]
        # Nous vérifions s'il y a un cycle
        # Pour ça on parcourt le graphe en partant de S1
        number_row = len(reel_quantity)
        number_column = len(reel_quantity[0])
        nombre_sommet = number_row + number_column
        # On commence à 1 car il faut prendre en compte le sommet S0
        compteur_sommets = 1
        nombre_de_sommets_a_parcourir = nombre_sommet - 1
        sommet_origine = Sommet_pied("S0", 1000000)

        sommet_actuel.parent = sommet_origine
        sommets_supr_nom = []
        trajet_envisageable = []
        sommets_supr_nom.append(sommet_actuel)
        # Si ce n'est pas connexe, on stock tout les graphs ici
        # On commence à parcourir le sommet actuel pour savoir où aller
        while nombre_de_sommets_a_parcourir + 1 > 0:
            # On veut voir où on peut aller
            for j in range(len(sommet_actuel.link_id)):
                # On regarde un sommet dans la liste des sommets
                index = sommet_actuel.link_id[j]
                prochain_sommet_nom = tab_sommet_id[index]
                prochain_sommet_nom.parent = sommet_actuel
                # On check si le prochain sommet n'est pas le prédécesseur (parent)

                if prochain_sommet_nom != sommet_actuel.parent:
                    # Si le prochain sommet n'est pas un parent, mais est un sommet où on est passé
                    if prochain_sommet_nom not in sommets_supr_nom:
                        trajet_envisageable.append(prochain_sommet_nom.id_sommet)

            # Maintenant qu'on a ajouté depuis notre somme ceux à quoi il est relié
            # On veut changer le sommet actuel parmi ceux disponibles, changer les sommets sup et set le parent
            if trajet_envisageable:
                # On fait effectivement le trajet
                sommet_actuel = tab_sommet_id[trajet_envisageable[0]]
                sommets_supr_nom.append(sommet_actuel)
                trajet_envisageable.pop(0)
                compteur_sommets += 1
                if compteur_sommets >= nombre_sommet:
                    return True, empty_tab

                else:
                    reel_quantity = [elem for elem in proposition_quantity if elem not in sommets_supr_nom]

            nombre_de_sommets_a_parcourir -= 1
        all_non_connex.append(sommets_supr_nom)

    # On veut supprimer du tableau all_non_connex les doublons
    # Créer une nouvelle matrice pour stocker les tableaux uniques
    matrice_sans_doublons = []

    # Parcourir chaque tableau dans la matrice initiale
    for tableau in all_non_connex:
        # Vérifier si le tableau est déjà dans la matrice sans doublons
        tableau_present = False
        for tableau_unique in matrice_sans_doublons:
            # Vérifier si les deux tableaux contiennent les mêmes éléments (même dans un ordre différent)
            if sorted(tableau, key=lambda x: x.id_sommet) == sorted(tableau_unique, key=lambda x: x.id_sommet):
                tableau_present = True
                break
        # Ajouter le tableau à la matrice sans doublons s'il n'est pas déjà présent
        if not tableau_present:
            matrice_sans_doublons.append(tableau)

    # Print des sous graphes
    # Parcourir chaque graphe isolé dans la matrice

    for sous_tableau in matrice_sans_doublons:
        # Récupérer les noms des sommets dans le sous-tableau
        noms_sommets = [sommet.nom_sommet for sommet in sous_tableau]
        # Afficher les noms des sommets
        # print(noms_sommets)

    """for i in range(len(sommets_supr_nom)):
        print("i", i)
        tab_part.append(sommets_supr_nom[i].nom_sommet)
        all_non_connex.append((tab_part))"""
    # tab_tempo = connexe(proposition_quantity, (tab_sommet_id - sommets_supr_nom)
    """for i in range(len(all_non_connex)):
        for j in range(len(all_non_connex[i])):
            print(all_non_connex)"""
    return False, matrice_sans_doublons


def verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id):
    # Nous vérifions si graphe contient moins de |V | − 1 arête (|V | étant le nombre de sommets).
    # Calcul nombre de sommets
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    nombre_sommet = number_row + number_column

    solution, le_cycle = acyclique(proposition_quantity, tab_sommet_id)
    if solution == False:
        pourquoi = "Le graphe est dégénéré car il contient un cycle."
        # Affichage du cycle
        print("Voici son cycle :")
        for sommet in le_cycle:
            print(sommet.nom_sommet, " ", end='')
        print("\n")
        return True, pourquoi

    # Calcul nombre d'arêtes
    nombre_arêtes = 0
    for i in range(number_row):
        for j in range(number_column):
            if proposition_quantity[i][j] != 0:
                nombre_arêtes += 1

    connexe_result, pas_important2 = connexe(proposition_quantity, tab_sommet_id)
    if connexe_result == False:
        pourquoi = "Le graphe est dégénéré car n'est pas connexe"
        return True, pourquoi

    # Si oui, il est dégénéré si graphe contient moins de |V| − 1 arête (|V | étant le nombre de sommets).
    """if nombre_arêtes < nombre_sommet - 1:
        pourquoi = "Le graphe est dégénéré car le graphe contient moins de |V| − 1 arête (|V| étant le nombre de sommets)."
        return True, pourquoi"""

    # print("Le graphe n'est pas dégénéré")
    pourquoi = ""
    return False, pourquoi


def supr_arrete(proposition_quantity, tab_sommet_id, le_cycle, tab_s, tab_c):
    tableau_arrete_sommet = []
    tableau_arete_nulles = []
    tableau_de_tableau_arete_nulles = []
    # On retrouve les valeurs des arêtes qui forment le cycle
    for i in range(len(le_cycle) - 1):
        # On veut récupérer les valeurs des sommets cycle dans la liste des sommets générale
        if le_cycle[i].nom_sommet.startswith("S"):
            tableau_arrete_sommet.append(
                proposition_quantity[le_cycle[i].id_sommet][le_cycle[i + 1].id_sommet - len(tab_s)])
        else:
            tableau_arrete_sommet.append(
                proposition_quantity[le_cycle[i + 1].id_sommet][le_cycle[i].id_sommet - len(tab_s)])

    # On cherche la valeur de l'arrete la plus petite sans compter 0
    tab_sans_zero = [valeur for valeur in tableau_arrete_sommet if valeur != 0]
    for i in range(len(tab_sans_zero)):
        print("Condition", i,":" , tab_sans_zero[i])
    tab_sans_zero = [tab_sans_zero[0], tab_sans_zero[-1]]
    plus_petit = min(tab_sans_zero)

    # On a la valeur à soustraire, maintenant, on veut effectivement la soustraire et l'additionner
    nombre_iterations = len(tableau_arrete_sommet)
    for i in range(nombre_iterations):
        if i % 2 == 0:
            tableau_arrete_sommet[i] -= plus_petit

        else:
            tableau_arrete_sommet[i] += plus_petit

    # Maintenant, on met les valeurs calculées dans la proposition de base
    for i in range(len(le_cycle) - 1):
        tableau_arete_nulles = []
        # On veut récupérer les valeurs des sommets cycle dans la liste des sommets générale
        if le_cycle[i].nom_sommet.startswith("S"):
            proposition_quantity[le_cycle[i].id_sommet][le_cycle[i + 1].id_sommet - len(tab_s)] = tableau_arrete_sommet[i]
            if tableau_arrete_sommet[i] == 0:
                tableau_arete_nulles.append(le_cycle[i].nom_sommet)
                tableau_arete_nulles.append(le_cycle[i + 1].nom_sommet)
                tableau_de_tableau_arete_nulles.append(tableau_arete_nulles)

        else:
            proposition_quantity[le_cycle[i + 1].id_sommet][le_cycle[i].id_sommet - len(tab_s)] = tableau_arrete_sommet[i]
            if tableau_arrete_sommet[i] == 0:
                tableau_arete_nulles.append(le_cycle[i].nom_sommet)
                tableau_arete_nulles.append(le_cycle[i + 1].nom_sommet)
                tableau_de_tableau_arete_nulles.append(tableau_arete_nulles)

    return tableau_de_tableau_arete_nulles


def rendre_connexe(proposition_quantity, tab_sommet_id, tab_s, tab_c, sous_tableau):
    # On fait un nombre de liens égal au nombre de different groupes de sommets
    for p in range(len(sous_tableau) - 1):
        # Si le premier element du sous tableau est un S
        if sous_tableau[p][0].nom_sommet.startswith("S"):
            # Alors on le relie avec un C
            # On regarde touts le éléments de tout les tableaux jusqu'à tomber sur un C
            for j in range(len(sous_tableau) - 1):
                j += 1
                for k in range(len(sous_tableau[j])):
                    if sous_tableau[j][k].nom_sommet.startswith("C"):
                        tab_sommet_id[sous_tableau[j][k].id_sommet].link_id.append(sous_tableau[p][0].id_sommet)
                        tab_sommet_id[sous_tableau[j][k].id_sommet].link.append(sous_tableau[p][0].nom_sommet)
                        tab_sommet_id[sous_tableau[p][0].id_sommet].link_id.append(sous_tableau[j][k].id_sommet)
                        tab_sommet_id[sous_tableau[p][0].id_sommet].link.append(sous_tableau[j][k].nom_sommet)

    return tab_sommet_id


def methode_du_marche_pied(proposition_quantity):
    # Création du graphe à partir du tableau
    print("Création du graphe et des sommets :")
    tab_c, tab_s, tab_sommet_id = graph_creation(proposition_quantity)
    print("\n")

    # Vérification si cyclique
    # Premier appel à acyclique
    acyclique_result, le_cycle = acyclique(proposition_quantity, tab_sommet_id)
    print("Il est cyclique :", not acyclique_result)

    if not acyclique_result:
        # S'il n'est pas cyclique
        # Affichage du cycle
        print("Voici son cycle :")
        for sommet in le_cycle:
            print(sommet.nom_sommet, " ", end='')
        print("\n")

        # On supprime alors une arête
        print("Suppression des arêtes :")
        tableau_arete_nulles = supr_arrete(proposition_quantity, tab_sommet_id, le_cycle, tab_s, tab_c)
        print("Voici les arrêtes supprimées :", tableau_arete_nulles)

        print("Voici notre nouvelle proposition :", proposition_quantity)
        tab_c, tab_s, tab_sommet_id = graph_creation(proposition_quantity)
        # On vérifie de nouveau s'il est cyclique
        the_acyclique_result, the_le_cycle = acyclique(proposition_quantity, tab_sommet_id)

        print("Il est cyclique :", not the_acyclique_result)
    print("\n")


    # Vérification si connexe
    est_connexe, sous_tableau = connexe(proposition_quantity, tab_sommet_id)
    print("Il est connexe :", est_connexe)
    # Affichage des liens
    if est_connexe == False:
        # Affichage des graphes
        print("Voici les sous graphes.")
        print("\n")
        for i in range(len(sous_tableau)):
            for j in range(len(sous_tableau[i])):
                print(sous_tableau[i][j].nom_sommet, end=' ')
            print("\n")
        print("On le rend connexe.")

        # Rendre connexe
        tab_sommet_id = rendre_connexe(proposition_quantity, tab_sommet_id, tab_s, tab_c, sous_tableau)

        # Affichage du nouveau graphe
        print("Voici les nouveaux liens")
        for p in range(len(tab_s)):
            print(tab_sommet_id[p].nom_sommet)
            print(tab_sommet_id[p].link)
    print("\n")


    # Vérification si dégénérée
    degenere, pourquoi = verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id)
    print("Il est dégénéré :", degenere)
    print(pourquoi)
    print("\n")

    return proposition_quantity
