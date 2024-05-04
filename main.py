from fonctions import *
from Methode_marche_pied import *

proposition_couts = [[5, 6, 7], [1, 9, 4]]
proposition_quantity = [[60, 20, 90], [0, 40, 50]]

# Création du graphe à partir du tableau
print("Création du graphe et des sommets :")
tab_c, tab_s, tab_sommet_id = graph_creation(proposition_quantity)
print("\n")

# Vérification si cyclique
acyclique, le_cycle = acyclique(proposition_quantity, tab_sommet_id)
print("Il est cyclique :", not acyclique)
if not acyclique:
    print("Voici son cycle :")
    for sommet in le_cycle:
        print(sommet.nom_sommet, " ", end='')
print("\n")




# Vérification si connexe
connexe, sous_tableau = connexe(proposition_quantity, tab_sommet_id)
print("Il est connexe :", connexe)
# Affichage des liens
for i in range(len(tab_sommet_id) - len(tab_c)):
    print("Liens de :", tab_sommet_id[i].nom_sommet)
    print(tab_sommet_id[i].link)
print("\n")


# Vérification si dégénérée
degenere, pourquoi = verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id)
print("Il est dégénéré :", degenere)
print(pourquoi)
print("\n")



# Création d'une arête nulle
"""for i in range(len(tab_s)):
    print("Link de :", tab_sommet_id[i].nom_sommet)
    print(tab_sommet_id[i].link_id)
for j in range(len(tab_c)):
    j += len(tab_s)
    print("Link de :", tab_sommet_id[j].nom_sommet)
    print(tab_sommet_id[j].link_id)"""
"""
# Je créé temporairement une arrête nulle en dure S2 C1
print("Création du fake sommet à 0 entre S2 et C1")
tab_sommet_id[2].link_id.append(tab_sommet_id[1].id_sommet)
tab_sommet_id[1].link_id.append(tab_sommet_id[2].id_sommet)"""

print("Suppression des arêtes :")
tableau_arete_nulles = supr_arrete(proposition_quantity, tab_sommet_id, le_cycle, tab_s, tab_c)
print("Voici les arrêtes supprimées :", tableau_arete_nulles)

print("Voici notre nouvelle proposition :", proposition_quantity)




"""while True:

    decoration_affichage("MENU PRINCIPAL :")
    print("1. Tester une proposition de problème de transport")
    print("2. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        num_proposition = int(input("Entrer le n° de proposition de problème de transport à tester (entre 1 et 12) : "))
        if 1 <= num_proposition <= 12:
            file_name= f'Propositions/proposition {num_proposition}.txt'
            decoration_affichage(f'Problème de transport N°{num_proposition}: \n')
            matrice=lecture_proposition(file_name)
            afficher_matrice(matrice)

        else:
            print("Numéro de proposition de problème de transport invalide. Veuillez entrer un numéro entre 1 et 12.")
    elif choix == "2":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")"""