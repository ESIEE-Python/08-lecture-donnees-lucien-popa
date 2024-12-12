"""module pour manipuler les csv"""
#### Imports et définition des variables globales
FILENAME = "listes.csv"
#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode = 'r', encoding='utf8') as f:
        for line in f:
            l.append([int(x) for x in line.split(";")])
    return l

def get_list_k(data, k):
    """retourne ke k-ieme element de la liste du fichier"""
    return data[k]

def get_first(l):
    """ retourne le premier element de la liste du fichier"""
    return l[0]

def get_last(l):
    """ retourne le dernier element de la liste du fichier"""
    return l[-1]

def get_max(l):
    """ retourne le maximum de la liste du fichier"""
    return max(l)

def get_min(l):
    """ retourne le minimum de la liste du fichier"""
    return min(l)

def get_sum(l):
    """retourne la somme des éléments d'une liste"""
    return sum(l)


#### Fonction principale


def main():
    """main"""
    print(read_data("listes.csv"))
    print(get_list_k(read_data("listes.csv"),0))
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
