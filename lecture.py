print("Lecture")

#Lecture du fichier
class Fichier:
    def __init__(self, fichiergrille):
        self.lignesfichier =''
        for i in fichiergrille:
            self.lignesfichier += ''.join(i).strip()
        self.lignesfichier = self.lignesfichier.replace(' ', '')
        for i in self.lignesfichier:
            assert i.isdigit() == True or i == '.', \
                'Le fichier grille ne doit contenir que des chiffres, des' \
                'points, des espaces ou des retour de lignes. Vérifiez l\'entrée'
    def imprimmer(self):
        print(self.lignesfichier)
    def convertirEnGrille(self):
        print('OK')

class Grille:
    def __init__(self, lignesfichier):
        self.dictionnaire = 2