sortie_fichier = True
nombre_min_lettres = 4

phrase = input("Écrivez une phrase : ")
liste_mots = phrase.split()

if len(liste_mots) == 0:
    print("Vous n'avez rien écrit")
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

    print(f"Proportion de mots avec {nombre_min_lettres} lettres ou plus : {proportion} %")

    if sortie_fichier:
        with open("resultat.txt", "w", encoding="utf-8") as f:
            for cle, valeur in informations.items():
                f.write(f"{cle} : {valeur}\n")