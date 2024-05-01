import pandas as pd
import numpy as np

matrice = []
def lecture_proposition(fichier):
    m = []
    dimensions = []
    num_ligne = 0
    with open(fichier, 'r') as f:
        for line in f:
            if num_ligne == 0:  # La première ligne contient les dimensions de la matrice
                dimensions.extend(map(int, line.split()))
            m.append([int(x) for x in line.split()])
            num_ligne+=1
        m.pop(0) # On retire la ligne des dimensions
        m[-1].append(sum(m[-1])) # Le problème étant équilibré on peut additionner la ligne ou la colonne, cela revient au même
    return m, dimensions

def matrice_couts(matrice):
    m = matrice
    m = m[:-1] # On prend tout sauf la dernière ligne
    for l in range(np.shape(m)[0]): # On parcours les lignes
        m[l] = m[l][:-1] # On prend tout sauf la dernière valeur
    return m

def afficher_proposition_transport(matrice):
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

    print(matrice)

def algo_nord_ouest(proposition_transport,dimensions):
    lignes, colonnes = dimensions # Correspond aux dimensions n,m dans la première ligne du fichier de proposition de transport
    solution = [[0] * (colonnes+1) for _ in range(lignes+1)] # Initialisation Matrice de répartitions des quantités
    i, j = 0, 0 # Initialisation des indices de ligne et de colonne

    proposition_transport_copie = [ligne[:] for ligne in proposition_transport]

    # Remet les valeurs des provisions et des commandes
    for i in range(lignes):
        solution[i][-1] = proposition_transport[i][-1]
    for j in range(colonnes):
        solution[-1][j] = proposition_transport[-1][j]
    # Remet la valeur de la somme totale
    solution[-1][-1] = proposition_transport[-1][-1]

    i, j = 0, 0  # Réinitialisation des indices de ligne et de colonne
    while i < lignes and j < colonnes:  # On va remplir le coin en haut à gauche au max à chaque itérations
        # On assigne la quantité à transporter selon les provisions et les commandes
        quantite = min(proposition_transport_copie[i][-1], proposition_transport_copie[-1][j])
        solution[i][j] = quantite
        # Pour mettre à jour les stocks disponibles
        proposition_transport_copie[i][-1] -= quantite
        proposition_transport_copie[-1][j] -= quantite
       
        # On passe à la ligne ou la colonne suivante s'il n'y a plus de provisions ou plus de commandes  
        if proposition_transport_copie[i][-1] == 0:
            i += 1
        elif proposition_transport_copie[-1][j] == 0:
            j += 1
    
    return solution

def algo_balas_hammer():
    # ici mettre algo de balas_hammer
    print("...")

def calcul_cout_total(matrice_cout,proposition_transport,dimensions):
    lignes,colonnes=dimensions
    cout_total=0
    details_cout = ""
    matrice_proposition = [l[:-1] for l in proposition_transport[:-1]]
    for i in range (lignes):
        for j in range (colonnes):
            if i != lignes - 1 or j != colonnes - 1:
                cout_partiel = matrice_cout[i][j] * matrice_proposition[i][j]
                cout_total += cout_partiel
                if cout_partiel !=0 :
                    details_cout += f"{matrice_cout[i][j]} × {matrice_proposition[i][j]} + "
            else:
                cout_partiel = matrice_cout[i][j] * matrice_proposition[i][j]
                cout_total += cout_partiel
                if cout_partiel !=0 :
                    details_cout += f"{matrice_cout[i][j]} × {matrice_proposition[i][j]}"
    print("\nDétails du calcul du coût total :")
    print(details_cout)
    print(f"Le coût total de la proposition est : {cout_total} €.")
    return cout_total
    
def decoration_affichage(message):
    print("\n" + "#"*50 + "\n")
    print(message)