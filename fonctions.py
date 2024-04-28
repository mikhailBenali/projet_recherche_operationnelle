import pandas as pd

matrice = []
def lecture_proposition(fichier):
    m = []
    with open(fichier, 'r') as f:
        for line in f:
            m.append([int(x) for x in line.split()])
        m.pop(0) # On retire la ligne des dimensions
        m[-1].append(sum(m[-1])) # Le problème étant équilibré on peut additionner la ligne ou la colonne, cela revient au même
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

def decoration_affichage(message):
    print("\n" + "#"*50 + "\n")
    print(message)