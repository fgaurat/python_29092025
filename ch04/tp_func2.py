def mult2(l:list[int]) ->list[int]:
    """
    Multiplie chaque élément d'une liste par 2.
    
    Args:
        l (list): Liste de nombres à multiplier par 2
        
    Returns:
        list: Nouvelle liste contenant chaque élément multiplié par 2
        
    Example:
        >>> mult2([1, 2, 3])
        [2, 4, 6]
    """
    # Initialise une liste vide pour stocker les résultats
    r = []
    
    # Parcourt chaque valeur de la liste d'entrée
    for value in l:
        # Multiplie la valeur par 2
        v = value * 2
        # Ajoute la nouvelle valeur à la liste de résultats
        r.append(v)
    
    # Retourne la liste des valeurs multipliées
    return r


def mult2_item(i):
    return i*2

# Liste de test avec des nombres entiers
l = [10, 20, 30, 40, 50]

# Appel de la fonction mult2 pour multiplier chaque élément par 2
r = mult2(l)  # Résultat attendu: [20, 40, 60, 80, 100]

# Affiche le résultat
print(r)

# r = map(mult2_item,l)
r = map(lambda v:v*2,l)
r = list(map(lambda v:v*2,l))
print(r)

