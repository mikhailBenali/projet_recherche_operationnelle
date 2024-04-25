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

matrice = lecture_proposition("./Propositions/proposition 1.txt")
print(pd.DataFrame(matrice))