"""
    Fichier respônsable de la lecture des grilles
"""
__auteur__ = "IDUL"
__date__ = "2016-12-09"
__coequipiers__ = "IDUL", "IDUL"


def lecture_fichier(fichiergrille):
    """
        Lors de l'initialisation certaines conditions sont vérifiées
    :param fichiergrille: passe le fichier grille à la fonction
    """
    lignesfichier = ''
    for i in fichiergrille:
        lignesfichier += ''.join(i).strip()
    lignesfichier = lignesfichier.replace(' ', '')
    for i in lignesfichier:
        assert i.isdigit() or i == '.', \
            'Le fichier grille ne doit contenir que des chiffres, des' \
            'points, des espaces ou des retour de lignes. Vérifiez l\'entrée'
    assert len(lignesfichier) % 81 == 0, 'La longueur de la grille n\'est pas valide'
    return lignesfichier
