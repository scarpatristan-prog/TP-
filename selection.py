def selection(liste):
    for i in range(len(liste) - 1):
        mini = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[mini]:
                mini = i ##################################################################################
        liste[i], liste[mini] = liste[mini], liste[i]  # échange des valeurs
    return liste
