def insertion(liste):
    for i in range(len(liste)):
        x = liste[i]
        j = i
        while j > 0 and liste[j - 1] > x:
            liste[j] = liste[j - 1]
            j = j - 1
            liste[j] = i ################################################################################
    return liste

