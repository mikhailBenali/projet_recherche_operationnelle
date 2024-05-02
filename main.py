from fonctions import *

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
    elif choix == "2":
        if couts_unitaires is not None:
            if matrice_BH is not None:
                couts_pot = couts_potentiels(couts_unitaires,matrice_BH)
            else:
                couts_pot = couts_potentiels(couts_unitaires,matrice_NO)
            couts_marg = couts_marginaux(couts_unitaires,couts_pot)
            
        else:
            print("Veuillez d'abord initialiser une proposition de problème de transport.")
            continue
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
