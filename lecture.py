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


class Grille:
    def __init__(self, lignesfichier):
        # Définitions de concepts généraux
        self.colonnes = "ABCDEFGHI"
        self.lignes = "123456789"
        self.nombres = self.lignes
        self.cases = self.produitCroise(self.lignes, self.colonnes)

        self.dictionnaire = 2
        self.valeurs = ""
    def convertirEnGrille(self):
        abs(1)

    def produitCroise(self, a, b):
        produit = []
        for i in a:
            for v in b:
                produit.append(i+v)
        return produit

