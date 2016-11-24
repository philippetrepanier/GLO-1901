print("Lecture")

##Lecture du fichier


class Fichier:
    def __init__(self, fichiergrille):
        self.lignesfichier = ''
        for i in fichiergrille:
            self.lignesfichier += ''.join(i).strip()
        self.lignesfichier = self.lignesfichier.replace(' ', '')
        for i in self.lignesfichier:
            assert i.isdigit() == True or i == '.', \
                'Le fichier grille ne doit contenir que des chiffres, des' \
                'points, des espaces ou des retour de lignes. Vérifiez l\'entrée'
        assert len(self.lignesfichier) % 81 == 0, 'La longueur de la grille n\'est pas valide'
    def imprimmer(self):
        print(self.lignesfichier)

    def convertirEnGrille(self):
        nombregrille = len(self.lignesfichier) // 81
        for i in nombregrille:


class Grille:
    def __init__(self, lignesfichier):
        self.dictionnaire = 2
        self.valeurs = ""