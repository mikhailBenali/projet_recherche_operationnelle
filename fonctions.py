import pandas as pd
import numpy as np

matrice = []
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

def afficher_matrice(matrice):
    print("\n")
    print(pd.DataFrame(matrice).to_string(index=False, header=False))

def balas_hammer(matrice):
    copie_matrice = np.array(matrice)
    
    # On calcule les pénalités
    penalites_provisions = []
    penalites_commandes = []
    
    for ligne in copie_matrice:
        ligne.sort()
        penalites_provisions.append(ligne[1] - ligne[0])
    
    copie_matrice = np.array(matrice)
    
    for colonne in np.transpose(copie_matrice):
        colonne.sort()
        penalites_commandes.append(colonne[1] - colonne[0])
    
    print("Pénalités provisions: ", penalites_provisions)
    print("Pénalités commandes: ", penalites_commandes)