import pandas as pd
import numpy as np
import random as rd

proposition = []
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

def balas_hammer(couts, proposition):
    copie_couts = np.array(couts)
    copie_proposition = np.array(proposition)
    
    copie_proposition[:-1,:-1] = 0 # Initialisation de la matrice de proposition à 0
    
    total = copie_proposition[-1,-1]
    
    provisions_initiales = copie_proposition[:,-1]
    commandes_initiales = copie_proposition[-1,:]
    
    provisions = provisions_initiales.copy()
    commandes = commandes_initiales.copy()
    
    def provisions_nulles(provisions,case):
        return provisions[case[0]] == 0
    def commandes_nulles(commandes,case):
        return commandes[case[1]] == 0
    
    while copie_proposition[:-1,:-1].sum() != total:
        
        # On calcule les pénalités
        penalites_lignes = []
        penalites_colonnes = []
        
        # On calcule les pénalités des lignes et des colonnes
        
        for i,ligne in enumerate(copie_couts):
            if not any(provisions_nulles(provisions,(i,j)) for j in range(len(ligne))) and provisions[i] != 0:
                ligne.sort()
                penalites_lignes.append(ligne[1] - ligne[0])
            else:
                penalites_lignes.append(0)
        
        copie_couts = np.array(couts)
        
        for j,colonne in enumerate(np.transpose(copie_couts)):
            if not any(provisions_nulles(provisions,(i,j)) for i in range(len(colonne))) and commandes[j] != 0:
                colonne.sort()
                penalites_colonnes.append(colonne[1] - colonne[0])
            else:
                penalites_colonnes.append(0)
        
        copie_couts = np.array(couts)
        
        penalite_max = -1
        
        # On trouve la plus grande pénalité
        
        penalite_max = max(penalites_lignes + penalites_colonnes)
        print("Pénalité maximale : ", penalite_max)
        
        # On trouve les coordonnées de la pénalité maximale
        
        print(f"Pénalités des lignes : {penalites_lignes}")
        print(f"Pénalités des colonnes : {penalites_colonnes}")
        
        coord_penalite_max_lignes = [i for i, j in enumerate(penalites_lignes) if j == penalite_max]
        print("Lignes de pénalité maximale : ", *[i for i in coord_penalite_max_lignes])
        coord_penalite_max_colonnes = [i for i, j in enumerate(penalites_colonnes) if j == penalite_max]
        print("Colonnes de pénalité maximale : ", *[i for i in coord_penalite_max_colonnes])
        
        coord_cas_cout_min_ligne = []
        coord_case_cout_min_colonne = []
        
        for ligne in coord_penalite_max_lignes:
            l = copie_couts[ligne].copy()
            l = [(ligne,colonne, l[colonne], min(provisions[ligne],commandes[colonne])) for colonne in range(len(l))]
            l_filtre = []
            for t in l:
                print(f"t[0] : {t[0]}, t[1] : {t[1]}, t[2] : {t[2]}, t[3] : {t[3]}")
                if t[3] == 0: # Si la capacité est nulle
                    l.remove(t)
            print(f"L : {l}")
            for t in l:
                if t[2] == min([t[2] for t in l]) and copie_proposition[t[0],t[1]] == 0: # Si le coût est minimal et que la case n'est pas remplie et que la capacité est non nulle
                    l_filtre.append(t)
            coord_cas_cout_min_ligne.extend(l_filtre)
            
        for colonne in coord_penalite_max_colonnes:
            c= np.transpose(copie_couts)[colonne].copy()
            c = [(ligne,colonne,c[ligne],min(provisions[ligne],commandes[colonne])) for ligne in range(len(c))]
            c_filtre = []
            for t in c:
                if t[3] == 0: # Si la capacité est nulle
                    l.remove(t)
            for t in c:
                if t[2] == min([t[2] for t in c]) and copie_proposition[t[0],t[1]] == 0:
                    c_filtre.append(t)
            coord_case_cout_min_colonne.extend(c_filtre)
        
        print(f"Cases de coût minimal dans les lignes de pénalité maximale : {coord_cas_cout_min_ligne}")
        print(f"Cases de coût minimal dans les colonnes de pénalité maximale : {coord_case_cout_min_colonne}")
        
        case_capacite_max = max(coord_cas_cout_min_ligne + coord_case_cout_min_colonne, key=lambda x:x[3])
        print(f"Case de capacité maximale : \n\nX : {case_capacite_max[0]}, Y : {case_capacite_max[1]}, Coût : {case_capacite_max[2]}, Capacité : {case_capacite_max[3]}\n")
        
        copie_proposition[case_capacite_max[0],case_capacite_max[1]] = case_capacite_max[3] # On remplit la case de coût minimal avec la capacité maximale
        
        provisions[case_capacite_max[0]] -= case_capacite_max[3] # On met à jour les provisions
        commandes[case_capacite_max[1]] -= case_capacite_max[3] # On met à jour les provisions
        
        # On met à jour les provisions et les commandes
        copie_proposition[-1,-1] = copie_proposition[:-1,:-1].sum()
        copie_proposition[:,-1] = provisions
        copie_proposition[-1,:] = commandes
        
        afficher_proposition_transport(copie_proposition)
        input()
        
    # On remet les valeurs des provisions et des commandes ainsi que la somme totale
    copie_proposition[:,-1] = provisions_initiales
    copie_proposition[-1,:] = commandes_initiales
    copie_proposition[-1,-1] = total
    
    return copie_proposition

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

    print(matrice, "\n")

def algo_nord_ouest(proposition_transport,dimensions):
    print("Rq : Les valeurs du tableau correspondent à la répartition des provisions (ce ne sont pas les coûts unitaires) \n")
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
    
def decoration_affichage(message):
    print("\n" + "#"*50 + "\n")
    print(message)