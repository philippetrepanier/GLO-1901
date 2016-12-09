"""
    Fichier respônsable de la lecture des grilles
"""
__auteur__ = "IDUL"
__date__ = "2016-12-09"
__coequipiers__ = "IDUL", "IDUL"


class Fichier:
    """
        Lecture des lignes du fichier grille. Sépare les grilles multiples
    """
    def __init__(self, fichiergrille):
        """
            Lors de l'initialisation certaines conditions sont vérifiées
        :param fichiergrille: passe le fichier grille à la fonction
        """
        self.lignesfichier = ''
        for i in fichiergrille:
            self.lignesfichier += ''.join(i).strip()
        self.lignesfichier = self.lignesfichier.replace(' ', '')
        for i in self.lignesfichier:
            assert i.isdigit() or i == '.', \
                'Le fichier grille ne doit contenir que des chiffres, des' \
                'points, des espaces ou des retour de lignes. Vérifiez l\'entrée'
        assert len(self.lignesfichier) % 81 == 0, 'La longueur de la grille n\'est pas valide'

    def imprimmer(self):
        print(self.lignesfichier)
