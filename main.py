from fonctions import *
from Methode_marche_pied import *

proposition_couts = [[5, 6, 7], [1, 9, 7]]
proposition_quantity = [[60, 20, 0], [10, 10, 0]]


proposition_quantity = methode_du_marche_pied(proposition_quantity)

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


couts_unitaires = None
proposition_transport = None
matrice_NO = None
matrice_BH = None

while True:
    decoration_affichage("MENU PRINCIPAL :")
    print("1. Initialiser une proposition de problème de transport")
    print("2. Appliquer la méthode du marche-pied")
    print("3. Quitter")

    choix = input("Entrez votre choix : ")

    # RESOLUTION PB DE TRANSPORT
    if choix == "1":
        num_proposition = int(input("Entrer le n° de proposition de problème de transport à initialiser (entre 1 et 12) : "))
        if 1 <= num_proposition <= 12:
            file_name= f'Propositions/proposition {num_proposition}.txt'
            decoration_affichage(f'Problème de transport N°{num_proposition}: \n')
            proposition_transport,dimensions=lecture_proposition(file_name)
            print("Rq : Les valeurs du tableau correspondent aux COÛTS \n")
            afficher_proposition_transport(proposition_transport)
            couts_unitaires=matrice_couts(proposition_transport)
            
            while True:
                decoration_affichage("Choisissez l'algorithme :")
                print("1. Nord-Ouest")
                print("2. Balas-Hammer")
                print("3. Revenir au menu principal")
                algo_choisi = input("Entrez votre choix : ")

                if algo_choisi == "1":
                    decoration_affichage("====== ALGORITHME NORD-OUEST ======\n")
                    matrice_NO=algo_nord_ouest(proposition_transport,dimensions)
                    print("Rq : Les valeurs du tableau correspondent aux QUANTITÉS \n")
                    afficher_proposition_transport(matrice_NO)
                    cout_total=calcul_cout_total(couts_unitaires,matrice_NO,dimensions)
                elif algo_choisi == "2":
                    decoration_affichage("====== ALGORITHME BALAS-HAMMER ======\n")
                    matrice_BH=algo_balas_hammer(couts_unitaires,proposition_transport)
                    print("Rq : Les valeurs du tableau correspondent aux QUANTITÉS \n")
                    afficher_proposition_transport(matrice_BH)
                    cout_total=calcul_cout_total(couts_unitaires,matrice_BH,dimensions)
                elif algo_choisi == "3":
                    print("Vous avez choisi de revenir au menu principal")
                    break
                else:
                    print("Choix invalide. Veuillez entrer 1 ou 2 pour choisir l'algorithme, ou entrer 3 pour revenir au menu principal.")
                    continue
        else:
            print("Numéro de proposition de problème de transport invalide. Veuillez entrer un numéro entre 1 et 12.")
    # MARCHE PIED AVEC CALCULS COUTS POTENTIELS & MARGINAUX
    elif choix == "2":
        while True:
                decoration_affichage("Choisissez l'algorithme :")
                print("1. Nord-Ouest")
                print("2. Balas-Hammer")
                print("3. Revenir au menu principal")
                algo_choisi = input("Entrez votre choix : ")

                if algo_choisi == "1":
                    num_proposition = int(input("Entrer le n° de proposition de problème de transport à initialiser (entre 1 et 12) : "))
                    if 1 <= num_proposition <= 12:
                        file_name= f'Propositions/proposition {num_proposition}.txt'
                        decoration_affichage(f'Problème de transport N°{num_proposition}: \n')
                        print("Rq : Les valeurs du tableau correspondent aux COÛTS \n")
                        proposition_transport,dimensions=lecture_proposition(file_name)
                        afficher_proposition_transport(proposition_transport)
                        couts_unitaires=matrice_couts(proposition_transport)
                        print("\n====== ALGORITHME NORD-OUEST ======\n")
                        matrice_NO=algo_nord_ouest(proposition_transport,dimensions)
                        print("Rq : Les valeurs du tableau correspondent aux QUANTITÉS \n")
                        afficher_proposition_transport(matrice_NO)
                        couts_pot = couts_potentiels(couts_unitaires,matrice_NO)
                        couts_marg = couts_marginaux(couts_unitaires,couts_pot)
                elif algo_choisi == "2":
                    num_proposition = int(input("Entrer le n° de proposition de problème de transport à initialiser (entre 1 et 12) : "))
                    if 1 <= num_proposition <= 13:
                        file_name= f'Propositions/proposition {num_proposition}.txt'
                        decoration_affichage(f'Problème de transport N°{num_proposition}: \n')
                        print("Rq : Les valeurs du tableau correspondent aux COÛTS \n")
                        proposition_transport,dimensions=lecture_proposition(file_name)
                        afficher_proposition_transport(proposition_transport)
                        couts_unitaires=matrice_couts(proposition_transport)
                        print("\n====== ALGORITHME BALAS-HAMMER ======\n")
                        matrice_BH=algo_balas_hammer(couts_unitaires,proposition_transport)
                        print("Rq : Les valeurs du tableau correspondent aux QUANTITÉS \n")
                        afficher_proposition_transport(matrice_BH)
                        couts_pot = couts_potentiels(couts_unitaires,matrice_BH)
                        couts_marg = couts_marginaux(couts_unitaires,couts_pot)
                elif algo_choisi == "3":
                    print("Vous avez choisi de revenir au menu principal")
                    break
                else:
                    print("Choix invalide. Veuillez entrer 1 ou 2 pour choisir l'algorithme, ou entrer 3 pour revenir au menu principal.")
                    continue
    elif choix == "3":
        print("Au revoir !")
        break
    else:

        print("Choix invalide. Veuillez entrer 1 ou 2.")
