def extraire(L1, L2):
    resultat = []
    for index in L2:
        if 0 <= index < len(L1):
            resultat.append(L1[index])
        else:
            resultat.append(None)
    return resultat