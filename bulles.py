def bulles(liste):
    flag = 0
    echange = 0
    while flag == 0:
        i = 0
        flag = 1
        while i+1 < len(liste):
            if liste[i] > liste[i+1]:
                liste[i],liste[i+1] = liste[i],liste[i+1] ##################################################
                flag = 0
                echange += 1
            i += 1
    return liste