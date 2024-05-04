from Type_marche_pied import *


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

            if prochain_sommet_nom != sommet_actuel.parent:
                # Si le prochain sommet n'est pas un parent, mais est un sommet où on est passé
                if prochain_sommet_nom in sommets_supr_nom:
                    # On cherche le cycle
                    # On se place sur un sommet appartenant au cycle et on l'ajoute au tableau cycle
                    sommet_actuel = prochain_sommet_nom
                    le_sommet_de_base_du_cycle = sommet_actuel
                    le_cycle.append(le_sommet_de_base_du_cycle)
                    longueur_a_faire = len(sommets_supr_nom)
                    print(le_cycle[i].nom_sommet)

                    # On fait ça pour tous les sommets qu'on a parcourus pour trouver s'il y avait un cycle
                    while longueur_a_faire > 0:
                        # On regarde si le sommet actuel a un enfant. Sinon il ne fait pas partie du cycle
                        if len(sommet_actuel.link_id) > 1:
                            # On cherche le premier enfant uniquement (le vrai sommet pas juste son id)
                            index = sommet_actuel.link_id[0]
                            prochain_sommet_nom = tab_sommet_id[index]
                            prochain_sommet_nom.parent = sommet_actuel
                            # Si le sommet où on se dirige est le parent, on recommence et on supprime le lien
                            if prochain_sommet_nom == sommet_actuel.parent:
                                temporaire = sommet_actuel.link_id[0]
                                sommet_actuel.link_id.pop(0)
                                index = sommet_actuel.link_id[0]
                                prochain_sommet_nom = tab_sommet_id[index]
                                prochain_sommet_nom.parent = sommet_actuel
                                sommet_actuel.link_id.insert(0, temporaire)
                            # On vérifie si on n'a pas fait le tour du cycle
                            if prochain_sommet_nom == le_sommet_de_base_du_cycle:
                                le_cycle.append(le_sommet_de_base_du_cycle)
                                return True, le_cycle
                            # On se déplace dedans
                            sommet_actuel = tab_sommet_id[prochain_sommet_nom.id_sommet]
                            le_cycle.append(sommet_actuel)

                        else:
                            print(sommet_actuel.nom_sommet)
                            # j'ai un doute que ce truc fonctionne
                            # On supprime le sommet des sommets restants et du cycle
                            sommets_supr_nom.remove(sommet_actuel)
                            le_cycle.remove(sommet_actuel)
                            sommet_actuel = sommet_actuel.parent

                        longueur_a_faire -= 1
                    print("J'ai pas trouvé le cycle : ", le_cycle)
                    return True, le_cycle

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
    return False, le_cycle


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
        print(noms_sommets)

    """for i in range(len(sommets_supr_nom)):
        print("i", i)
        tab_part.append(sommets_supr_nom[i].nom_sommet)
        all_non_connex.append((tab_part))"""
    # tab_tempo = connexe(proposition_quantity, (tab_sommet_id - sommets_supr_nom)
    """for i in range(len(all_non_connex)):
        for j in range(len(all_non_connex[i])):
            print(all_non_connex)"""
    return False, matrice_sans_doublons

"""
def rendre_connexe(proposition_quantity, tab_sommet_id, tab_s, tab_c):
    is_ok_1 = False
    is_ok_2 = False
    is_connexe, sous_tableau = connexe(proposition_quantity, tab_sommet_id)
    # On fait un nombre de liens égal au nombre de different groupes de sommets
    print("len tab p", len(sous_tableau))
    for p in range(len(sous_tableau)):
        print("len tab s", len(tab_s))
        # Pour parcourir tous les S pour où ajouter
        for i in range(len(tab_s)):
            print("i suivant")
            # Pour parcourir tous les C pour les ajouter
            # print(len(tab_sommet_id) - len(tab_s))
            for j in range(len(tab_sommet_id) - len(tab_s)):
                j += len(tab_s)
                # Pour parcourir tous les enfants de là où on va ajouter
                for k in range(len(tab_sommet_id[i].link_id)):
                    if tab_sommet_id[i].link_id[k] != tab_sommet_id[j].id_sommet:
                        # On relie les deux
                        tab_sommet_id[i].link_id.append(tab_sommet_id[j].id_sommet)
                        tab_sommet_id[j].link_id.append(tab_sommet_id[i].id_sommet)
                        tab_sommet_id[i].link_id = list(set(tab_sommet_id[i].link_id))
                        tab_sommet_id[j].link_id = list(set(tab_sommet_id[j].link_id))

                        # Seulement si on ajouté le bon nombre de sommets (3 groupes, 2 liaisons)
                        if p == len(sous_tableau) - 2:
                            is_ok_1 = connexe(proposition_quantity, tab_sommet_id)
                            is_ok_2 = acyclique(proposition_quantity, tab_sommet_id)

                    else:
                        print('a')

    if is_ok_1:
        if is_ok_2:
            return tab_sommet_id
    print("C'est impossible")
    return tab_sommet_id"""


def verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id):
    # Nous vérifions si graphe contient moins de |V | − 1 arête (|V | étant le nombre de sommets).
    # Calcul nombre de sommets
    number_row = len(proposition_quantity)
    number_column = len(proposition_quantity[0])
    nombre_sommet = number_row + number_column

    solution = acyclique(proposition_quantity, tab_sommet_id)
    if not solution:
        print("Le graphe est dégénéré car il contient un cycle.")
        return True

    # Calcul nombre d'arêtes
    nombre_arêtes = 0
    for i in range(number_row):
        for j in range(number_column):
            if proposition_quantity[i][j] != 0:
                nombre_arêtes += 1

    # Si oui, il est dégénéré si graphe contient moins de |V | − 1 arête (|V | étant le nombre de sommets).
    if nombre_arêtes < nombre_sommet - 1:
        print(
            "Le graphe est dégénéré car le graphe contient moins de |V | − 1 arête (|V | étant le nombre de sommets).")
        return True

    print("Le graphe n'est pas dégénéré")
    return False


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


"""for i in range(nombre_iterations):
    if le_cycle[0].nom_sommet.startswith("S"):
        if i % 2 == 0:
            tableau_arrete_sommet[i] += 10
            print(tableau_arrete_sommet[i])
        else:
            tableau_arrete_sommet[i] -= 10
            print(tableau_arrete_sommet[i])
    else:
        if i % 2 == 0:
            tableau_arrete_sommet[i] += 10
            print(tableau_arrete_sommet[i])
        else:
            tableau_arrete_sommet[i] -= 10
            print(tableau_arrete_sommet[i])"""

""" debut_arrete_cycle = le_cycle[i].id_sommet
fin_arrete_cycle = le_cycle[i + 1].id_sommet
# On veut savoir si le premier commence par un C ou un S
    debut_arrete_cycle_vrai = tab_sommet_id[debut_arrete_cycle]
    fin_arrete_cycle_vrai = tab_sommet_id[fin_arrete_cycle]
    proposition_quantity[debut_arrete_cycle_vrai][fin_arrete_cycle_vrai]
else:
    debut_arrete_cycle_vrai = len(tab_sommet_id[debut_arrete_cycle]) + len(tab_s)
    fin_arrete_cycle_vrai = len(tab_sommet_id[fin_arrete_cycle])
    valeur_de_mon_arrete = proposition_quantity[debut_arrete_cycle_vrai][fin_arrete_cycle_vrai]
print(valeur_de_mon_arrete)

"""

# Une fois qu'on a récupéré dans la liste générale on regarde sa valeur dans le tableau


# S'il commence par un C on sait qu'il faut chercher dans la deuxième partie du tableau
# On a donc récupérer leur réel emplacement dans tab_sommet_id et on peut retrouver les bons sommets
