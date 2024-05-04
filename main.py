from fonctions import *
from Methode_marche_pied import *

"""proposition_couts = [[5,7,8],[6,8,5],[6,7,7]]
proposition_quantity = [[25,0,0,25],[10,15,0,25],[0,5,20,25],[35,20,20,75]]
cout_pot=[[5,7,7],[6,8,8],[5,7,7]]"""


proposition_couts= [[11, 12, 10, 10], [17, 16, 15, 18], [19, 21, 20, 22]]
proposition_quantity= [[50, 10, 0, 0], [0, 30, 0, 0], [0, 35, 30, 25]]
cout_pot= [[11, 12, 11, 13], [15, 16, 15, 17], [20, 21, 20, 22]]

proposition_quantity = methode_du_marche_pied(proposition_quantity, proposition_couts)

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
