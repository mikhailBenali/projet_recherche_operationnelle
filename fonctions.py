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
    
    # On trouve la plus grande pénalité
    
    penalite_max = max(penalites_lignes + penalites_colonnes)
    
    penalites_max_lignes = [penalite == penalite_max for penalite in penalites_lignes]
    penalites_max_colonnes = [penalite == penalite_max for penalite in penalites_colonnes]
    
    # Si la pénalité maximale est présente plusieurs fois dans les pénalités des lignes ou colonnes
    # On trouve les coordonnées des cases de coût minimal dans ces lignes ou colonnes
    # On parcourt les cases de coût minimal
    # On calcule le minimum des provisions et des commandes de chaque case
    # On choisit le maximum de toutes ces provisions et commandes
    # On remplit la case de coût minimal avec ce maximum
    
    cases_cout_min_lignes = []
    cases_cout_min_colonnes = []
    
    if [penalites_max_lignes+penalites_max_colonnes].count(True) > 1: # Si la pénalité maximale est présente plusieurs fois
        # On note les coordonnées des cases de coût minimal de chaque ligne ou colonne
        for i in range(len(penalites_max_lignes)):
            if penalites_max_lignes[i]:
                cases_cout_min_lignes.append((i,np.argmin(copie_couts[i]))) # On ajoute les coordonnées de la case de coût minimal
        for j in range(len(penalites_max_colonnes)):
            if penalites_max_colonnes[j]:
                cases_cout_min_colonnes.append((np.argmin(np.transpose(copie_couts)[j]),j)) # Idem
    
    capacites_min_lignes = [] # On stocke les minimums de capacité de provisions et commandes de chaque case de coût minimal dans les provisions de pénalité maximale
    capacites_min_colonnes = [] # Idem pour les commandes de pénalité maximale
    
    for case_min in cases_cout_min_lignes:
        capacites_min_lignes.append(min(copie_proposition[case_min[0]][-1], copie_proposition[-1][case_min[1]])) # On ajoute le minimum des provisions et des commandes de chaque case
    for case_min in cases_cout_min_colonnes:
        capacites_min_colonnes.append(min(copie_proposition[case_min[0]][-1], copie_proposition[-1][case_min[1]]))
    
    # On choisit les coordonnées du maximum de toutes ces capacités
    
    capacite_max_lignes = np.argmax(capacites_min_lignes)
    capacite_max_colonnes = np.argmax(capacites_min_colonnes)
    
    if copie_proposition[capacite_max_lignes[0]][capacite_max_lignes[1]] > copie_proposition[capacite_max_colonnes[0]][capacite_max_colonnes[1]]:
        copie_proposition[capacite_max_lignes[0]] = 0
        copie_proposition[cases_cout_min_lignes[0]][cases_cout_min_lignes[1]] = copie_proposition[capacite_max_lignes[0]][capacite_max_lignes[1]] # Si la capacité maximale est dans les lignes
    else:
        copie_proposition[:,capacite_max_colonnes[1]] = 0
        copie_proposition[np.argmin(copie_couts[capacite_max_colonnes[0]])][capacite_max_colonnes[0]] = copie_proposition[capacite_max_colonnes[0]][capacite_max_colonnes[1]] # Si la capacité maximale est dans les lignes

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
