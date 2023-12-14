import re

def recherche_mot_regex(chaine, mot):
    pattern = re.compile(r'\b{}\b'.format(re.escape(mot)))
    return bool(pattern.search(chaine))



# Exemple d'utilisation
chaine_test = "Bellingham meilleur joueur"
mot_test = "Bellingham"
resultat = recherche_mot_regex(chaine_test, mot_test)
print(resultat)  
