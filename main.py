from fonctions import *
from Methode_marche_pied import *

proposition_quantity = [[10, 10, 0], [0, 0, 0]]

tab_c, tab_s, tab_sommet_id = graph_creation(proposition_quantity)
degenere = verif_degenerecance(proposition_quantity, tab_s, tab_c, tab_sommet_id)
print("Il est dégénéré :", degenere)
connexe = connexe(proposition_quantity, tab_sommet_id)
print("Il est connexe :", connexe)

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