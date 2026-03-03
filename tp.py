classeur = {"negatifs": [], "positifs": []}

def trier(classeur, valeur):
    if valeur < 0:
        classeur["negatifs"].append(valeur)
    else:
        classeur["positifs"].append(valeur)
    return classeur

def difference(L1, L2):
    diff1 = [x for x in L1 if x not in L2]
    diff2 = [x for x in L2 if x not in L1]
    return (diff1, diff2)