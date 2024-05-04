import pandas as pd
import numpy as np
import random as rd

proposition = []

def decoration_affichage(message):
    print("\n" + "#"*50 + "\n")
    print(message)

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
        noms_lignes.append(f'S{j+1}')
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

def algo_balas_hammer(couts, proposition):
    copie_couts = np.array(couts)
    copie_proposition = np.array(proposition)
    
    copie_proposition[:-1,:-1] = 0 # Initialisation de la matrice de proposition à 0
    
    total = copie_proposition[-1,-1]
    
    provisions_initiales = copie_proposition[:,-1].copy()
    commandes_initiales = copie_proposition[-1,:].copy()
    
    provisions = provisions_initiales.copy()
    commandes = commandes_initiales.copy()
    
    while copie_proposition[:-1,:-1].sum() != total:
        
        # On calcule les pénalités
        penalites_lignes = []
        penalites_colonnes = []
        
        # On calcule les pénalités des lignes et des colonnes
        
        for i,ligne in enumerate(copie_couts):
            if not provisions[i] == 0:
                ligne.sort()
                penalites_lignes.append(ligne[1] - ligne[0])
            else:
                penalites_lignes.append(0)
        
        copie_couts = np.array(couts)
        
        for j,colonne in enumerate(np.transpose(copie_couts)):
            if not commandes[j] == 0:
                colonne.sort()
                penalites_colonnes.append(colonne[1] - colonne[0])
            else:
                penalites_colonnes.append(0)
        
        copie_couts = np.array(couts)
        
        penalite_max = -1
        
        # On trouve la plus grande pénalité
        
        penalite_max = max(penalites_lignes + penalites_colonnes)
        
        # On trouve les coordonnées de la pénalité maximale
        
        coord_penalite_max_lignes = [i for i, j in enumerate(penalites_lignes) if j == penalite_max]
        coord_penalite_max_colonnes = [i for i, j in enumerate(penalites_colonnes) if j == penalite_max]
        
        coord_cas_cout_min_ligne = []
        coord_case_cout_min_colonne = []
        
        for ligne in coord_penalite_max_lignes:
            
            l = copie_couts[ligne].copy()
            l = [(ligne,colonne, l[colonne], min(provisions[ligne],commandes[colonne])) for colonne in range(len(l))] # On ajoute les coordonnées de la case, le coût, et la capacité minimale
            
            l_filtre = [tup for tup in l if tup[3] != 0] # On filtre les cases de coût minimal en retirant celles qui ont une capacité nulle
            # On filtre les cases de coût minimal en retirant celles qui ont déjà été remplies ou qui n'ont pas un coût minimal
            l_filtre = [tup for tup in l_filtre if tup[2] == min([tup[2] for tup in l_filtre]) and copie_proposition[tup[0],tup[1]] == 0]
            coord_cas_cout_min_ligne.extend(l_filtre)
            
        for colonne in coord_penalite_max_colonnes:
            c= np.transpose(copie_couts)[colonne].copy()
            c = [(ligne,colonne,c[ligne],min(provisions[ligne],commandes[colonne])) for ligne in range(len(c))]
            
            c_filtre = [tup for tup in c if tup[3] != 0]
            c_filtre = [tup for tup in c_filtre if tup[2] == min([tup[2] for tup in c_filtre]) and copie_proposition[tup[0],tup[1]] == 0]
            coord_case_cout_min_colonne.extend(c_filtre)
        
        case_capacite_max = max(coord_cas_cout_min_ligne + coord_case_cout_min_colonne, key=lambda x:x[3])
        
        copie_proposition[case_capacite_max[0],case_capacite_max[1]] = case_capacite_max[3] # On remplit la case de coût minimal avec la capacité maximale
        
        provisions[case_capacite_max[0]] -= case_capacite_max[3] # On met à jour les provisions
        commandes[case_capacite_max[1]] -= case_capacite_max[3] # On met à jour les provisions
        
        # On met à jour les provisions et les commandes
        copie_proposition[-1,-1] = copie_proposition[:-1,:-1].sum()
        copie_proposition[:,-1] = provisions
        copie_proposition[-1,:] = commandes
        
    # On remet les valeurs des provisions et des commandes ainsi que la somme totale
    copie_proposition[:,-1] = provisions_initiales
    copie_proposition[-1,:] = commandes_initiales
    copie_proposition[-1,-1] = total
    
    return copie_proposition

def calcul_cout_total(matrice_cout,proposition_transport,dimensions):
    lignes,colonnes=dimensions
    cout_total=0
    matrice_proposition = [l[:-1] for l in proposition_transport[:-1]]
    print("\nDétails du calcul du coût total :")
    for i in range (lignes):
        for j in range (colonnes):
            cout_partiel = matrice_cout[i][j] * matrice_proposition[i][j]
            if cout_partiel != 0:
                cout_total += cout_partiel
                if cout_total != cout_partiel:  # Vérif si ce n'est pas la première valeur ajoutée
                    print(" + ", end="")
                print(f"{matrice_cout[i][j]} × {matrice_proposition[i][j]}", end="")
    print(f"\nLe coût total de la proposition est : {cout_total} €.")
    return cout_total

def capacite_case(x,y,proposition):
    return min(proposition[x][-1],proposition[-1][y])

def couts_potentiels(couts,proposition):
    decoration_affichage("====== Calcul des potentiels ======")
    print("\n=> Système linéaire pour le calcul des potentiels :")
    # Affichage du système linéaire
    for i in range(len(proposition)-1):
        for j in range(len(proposition[i])-1):
            if proposition[i][j] != 0:
                print(f"E(S{i+1}) - E(C{j+1}) = {couts[i][j]}")

    # On parcourt les lignes et les colonnes de la matrice de proposition
    # On stocke les indices des cases non nulles leur coût et leur demande
    
    arretes = []
    
    for i in range(len(proposition)-1):
        for j in range(len(proposition[i])-1):
            if proposition[i][j] != 0:
                arretes.append((i,j,couts[i][j]))
    
    # On initialise les listes A (coefficients des variables) et B (résultats des équations)
    A = np.zeros((len(couts)+len(couts[0]),len(couts)+len(couts[0])))
    B = []
    
    for i in range(len(arretes)):
        x,y,d = arretes[i]
        A[i][x] = 1
        A[i][y+len(couts)] = -1
        B.append(d)
    
    # On définit le coût potentiel de la première case à 0
    A[-1][0] = 1 
    B.append(0)
    print("E(S1) = 0")
    
    solution = np.linalg.solve(A,B)
    
    couts_pot = np.zeros((len(couts),len(couts[0])))
    
    for i in range(len(couts)):
        for j in range(len(couts[i])):
            couts_pot[i][j] = solution[i] - solution[j+len(couts)]

    print("\n=> Résolution du système linéaire :")
    # Affichage de la résolution du système
    for i in range(len(couts)):
        print(f"E(S{i+1}) =", int(solution[i]))
    for i in range(len(proposition)-1):
        print(f"E(C{i+1}) =", int(solution[len(couts)+i]))
    
    print("\n=> Matrice des coûts potentiels :\n")
    tab_couts_pot=pd.DataFrame(couts_pot.astype(int), index=[f"S{i+1}" for i in range(len(couts))], columns=[f"C{i+1}" for i in range(len(couts[0]))])
    print(tab_couts_pot)
    return couts_pot

def couts_marginaux(couts,couts_potentiels):
    "return [couts[i][j] - couts_potentiels[i][j] for i in range(len(couts)) for j in range(len(couts[i]))]"
    couts_marg = []
    for i in range(len(couts)):
        row = []
        for j in range(len(couts[i])):
            cout_marginal = int(couts[i][j] - couts_potentiels[i][j])
            row.append(cout_marginal)
        couts_marg.append(row)
    print("\n=> Matrice des coûts marginaux :\n")
    tab_couts_marg=pd.DataFrame(couts_marg, index=[f"S{i+1}" for i in range(len(couts))], columns=[f"C{i+1}" for i in range(len(couts[0]))])
    print(tab_couts_marg)
    return couts_marg

def verif_cout_marginal_positif(couts_marginaux):
    for i in range(len(couts_marginaux)):
        for j in range(len(couts_marginaux[i])):
            if proposition[i][j] < 0:
                return False
    return True