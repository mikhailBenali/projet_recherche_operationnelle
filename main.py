from fonctions import *
from Methode_marche_pied import *

proposition_quantity = [[20, 20, 20], [0, 30, 40]]

# Création du graphe à partir du tableau
tab_c, tab_s, tab_sommet_id = graph_creation(proposition_quantity)


# Vérification si dégénérée
degenere = verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id)
print("Il est dégénéré :", degenere)

# Vérification si cyclique
acyclique, le_cycle = acyclique(proposition_quantity, tab_sommet_id)
print("Il est cyclique :", acyclique)
if not acyclique:
    for sommet in le_cycle:
        print(sommet.nom_sommet, " ", end='')
    print("\n")

# Vérification si connexe
connexe, sous_tableau = connexe(proposition_quantity, tab_sommet_id)

print("Il est connexe :", connexe)
if not connexe:
    print("sous tableaux :", sous_tableau)
#    tab_sommet_id = rendre_connexe(proposition_quantity, tab_sommet_id, tab_s, tab_c)
    """for i in range(len(tab_sommet_id)):
        print("Liens de :", tab_sommet_id[i].nom_sommet)
        print(tab_sommet_id[i].link_id)
    print("Fin algo connexe :",)"""


for i in range(len(tab_s)):
    print("Link de :", tab_sommet_id[i].nom_sommet)
    print(tab_sommet_id[i].link_id)
for j in range(len(tab_c)):
    j += len(tab_s)
    print("Link de :", tab_sommet_id[j].nom_sommet)
    print(tab_sommet_id[j].link_id)
"""
# Je créé temporairement une arrête nulle en dure S2 C1
print("Création du fake sommet à 0 entre S2 et C1")
tab_sommet_id[2].link_id.append(tab_sommet_id[1].id_sommet)
tab_sommet_id[1].link_id.append(tab_sommet_id[2].id_sommet)"""

"""
tableau_arete_nulles = supr_arrete(proposition_quantity, tab_sommet_id, le_cycle, tab_s, tab_c)
print("Voici les arrêtes supprimées :", tableau_arete_nulles)
print(proposition_quantity)
"""
"""
while True:

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