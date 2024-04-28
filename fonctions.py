import pandas as pd
import numpy as np
import random as rd

proposition = []
def lecture_proposition(fichier):
    m = []
    with open(fichier, 'r') as f:
        for line in f:
            m.append([int(x) for x in line.split()])
        m.pop(0) # On retire la ligne des dimensions
        # Le problème étant équilibré on peut additionner la ligne ou la colonne, cela revient au même
        m[-1].append(sum(m[-1])) 
    return m

def matrice_couts(matrice):
    m = matrice
    m = m[:-1] # On prend tout sauf la dernière ligne
    for l in range(np.shape(m)[0]): # On parcours les lignes
        m[l] = m[l][:-1] # On prend tout sauf la dernière valeur
    return m

def balas_hammer(couts, copie_proposition):
    copie_couts = np.array(couts)
    copie_proposition = np.array(copie_proposition)
    
    copie_proposition[:-1,:-1] = 0
    afficher_matrice(copie_proposition)
    
    # On calcule les pénalités
    penalites_lignes = []
    penalites_colonnes = []
    
    for ligne in copie_couts:
        ligne.sort()
        penalites_lignes.append(ligne[1] - ligne[0])
    
    copie_couts = np.array(couts)
    
    for colonne in np.transpose(copie_couts):
        colonne.sort()
        penalites_colonnes.append(colonne[1] - colonne[0])
    
    copie_couts = np.array(couts)
    
    penalite_max = -1
    
    while any([i == 0 for i in copie_proposition[:-1,:-1].flatten()]):
    
        # On trouve la plus grande pénalité
        
        penalite_max = max(penalites_lignes + penalites_colonnes)
        print("Pénalité maximale : ", penalite_max)
        
        # On trouve les coordonnées de la pénalité maximale
        
        coord_penalite_max_lignes = [i for i, j in enumerate(penalites_lignes) if j == penalite_max]
        print("Lignes de pénalité maximale : ", *[i+1 for i in coord_penalite_max_lignes])
        coord_penalite_max_colonnes = [i for i, j in enumerate(penalites_colonnes) if j == penalite_max]
        print("Colonnes de pénalité maximale : ", *[i+1 for i in coord_penalite_max_colonnes])
        
        # Si la pénalité maximale est présente plusieurs fois dans les pénalités des lignes ou colonnes
        #if len(coord_penalite_max_lignes) > 1 or len(coord_penalite_max_colonnes) > 1:
            # On trouve les coordonnées des cases de coût minimal dans ces lignes ou colonnes
        coord_cas_cout_min_ligne = []
        coord_case_cout_min_colonne = []
        for ligne in coord_penalite_max_lignes:
            coord_cas_cout_min_ligne  = [(ligne,i) for i, j in enumerate(copie_couts[ligne]) if j == min(copie_couts[ligne])]
        for colonne in coord_penalite_max_colonnes:
            coord_case_cout_min_colonne = [(i,colonne) for i, j in enumerate(copie_couts[:,colonne]) if j == min(copie_couts[:,colonne])]
        # On parcourt les cases de coût minimal
        capacites_ligne = []
        capacites_colonne = []
        # On trouve les capacités des lignes correspondant aux cases de coût minimal
        for case in coord_cas_cout_min_ligne:
            # On trouve les provisions et commandes de la case
            provision = copie_proposition[case[0]][-1]
            commande = copie_proposition[-1][case[1]]
            # On calcule le minimum des provisions et des commandes
            capacites_ligne.append((case[0],case[1],min(provision, commande)))
        # Idem pour les colonnes
        for case in coord_case_cout_min_colonne:
            # On trouve les provisions et commandes de la case
            provision = copie_proposition[case[0]][-1]
            commande = copie_proposition[-1][case[1]]
            # On calcule le minimum des provisions et des commandes
            capacites_colonne.append((case[0],case[1],min(provision, commande)))
        # On choisit le maximum de toutes ces provisions et commandes (ainsi que les coordonnées de la case correspondante)
        capacite_max_lignes = []
        capacite_max_colonnes = []
        
        if capacites_ligne != []:
            capacite_max_lignes = max(capacites_ligne, key=lambda x:x[2]) # On prend le maximum des capacités
        if capacites_colonne != []:
            capacite_max_colonnes = max(capacites_colonne, key=lambda x:x[2]) # On prend le maximum des capacités
        
        print("Capacité maximale des lignes : ", capacite_max_lignes)
        print("Capacité maximale des colonnes : ", capacite_max_colonnes)
        
        # On remplit la case de coût minimal avec ce maximum
        if capacite_max_lignes != [] and capacite_max_colonnes != []:
            print("Les deux capacités maximales sont présentes")
            if capacite_max_lignes[2] > capacite_max_colonnes[2]: # Si la capacité maximale est dans les lignes
                copie_proposition[capacite_max_lignes[0]][capacite_max_lignes[1]] = capacite_max_lignes[2] # On remplit la case
                # On mets des 0 dans le reste de la ligne
                print(copie_proposition[capacite_max_lignes[0],:-1])
                copie_proposition[capacite_max_lignes[0],:-1] = 0
            elif capacite_max_colonnes[2] > capacite_max_lignes[2] :
                copie_proposition[capacite_max_colonnes[0]][capacite_max_colonnes[1]] = capacite_max_colonnes[2]
                # On mets des 0 dans le reste de la colonne
                print(copie_proposition[:-1,capacite_max_colonnes[1]])
                copie_proposition[:-1,capacite_max_colonnes[1]] = 0
        elif capacite_max_lignes != []:
            print("La capacité maximale des lignes est présente")
            copie_proposition[capacite_max_lignes[0]][capacite_max_lignes[1]] = capacite_max_lignes[2] # On remplit la case
            # On mets des 0 dans le reste de la ligne
            print(copie_proposition[capacite_max_lignes[0],:-1])
            copie_proposition[capacite_max_lignes[0],:-1] = 0
        elif capacite_max_colonnes != []:
            print("La capacité maximale des colonnes est présente")
            copie_proposition[capacite_max_colonnes[0]][capacite_max_colonnes[1]] = capacite_max_colonnes[2]
            # On mets des 0 dans le reste de la colonne
            print(copie_proposition[:-1,capacite_max_colonnes[1]])
            copie_proposition[:-1,capacite_max_colonnes[1]] = 0
        
        afficher_matrice(copie_proposition)

def afficher_matrice(matrice):
    print()
    # Noms des colonnes
    noms_colonnes = []
    for i in range(len(matrice[0])):
        noms_colonnes.append(f'C{i+1}')


    # Noms des lignes
    noms_lignes = []
    for j in range(len(matrice)):
        noms_lignes.append(f'P{j+1}')
        
    matrice=pd.DataFrame(matrice, columns=noms_colonnes, index=noms_lignes)
    provisions = matrice.columns[-1]
    matrice = matrice.rename(columns={provisions: 'Provisions'})
    commandes = matrice.index[-1]
    matrice = matrice.rename(index={commandes: 'Commandes'})

    print(matrice, "\n")

def decoration_affichage(message):
    print("\n" + "#"*50 + "\n")
    print(message)
