def calcul_mots_long(phrase, nombre_min_lettres = 4):
    """
    Prend en entrée un texte phrase et renvoie le nombre de mots longs
    """
    liste_mots = phrase.split()
    
    if len(liste_mots) == 0:
        print("Vous n'avez rien écrit")
        return None
    else:
        nombre_mots = len(liste_mots)
        compteur = 0
        for mot in liste_mots:
            mot_nettoye = mot.strip(".,;:!?«»\"'()")
            if len(mot_nettoye) >= nombre_min_lettres:
                compteur += 1
    
        proportion = round(100 * compteur / nombre_mots, 2)
        informations = {
            "Total": compteur,
            "Proportion": proportion,
            "Phrase": phrase,
            "Seuil": nombre_min_lettres,
        }
        return informations

def ecrire_coucou():
    print("Coucou")