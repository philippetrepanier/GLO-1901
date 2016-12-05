# Ce fichier est responsable de la résolution du sudoku par backtracking
#petite fleur sèche
print("Solver")


class Grille:
    def __init__(self, lignesfichier):
        # Définitions de concepts généraux
        self.colonnes = "123456789"
        self.lignes = "ABCDEFGHI"
        self.cases = {}
        self.grillevide = {}

        compte = 0
        for l in self.lignes:
            self.cases[l] = {}
            self.grillevide[l] ={}
            for c in self.colonnes:
                if lignesfichier[compte] == "." or lignesfichier[compte] == "0":
                    self.cases[l][c] = self.colonnes
                else:
                    self.cases[l][c] = lignesfichier[compte]
                self.grillevide[l][c] = ''
                compte += 1
        self.reduire()

    def reduire(self):
        grille_réduite = self.grillevide.copy()
        for l, v in self.cases.items():
            for c, n in v.items():
                if len(n) == 1:
                    for l2 in self.lignes:
                        if l2 != l:
                            if self.cases[l][c] == self.cases[l2][c]:
                                return False
                            else:
                                grille_réduite[l2][c] = self.cases[l2][c].replace(str(self.cases[l][c]), 'pou')
                    for c2 in self
                else:
                    continue


        print(grille_réduite)
        return grille_réduite


    # Permet de vérifier si toute la grille contient un élément
    def resolu(self):
        for l, v in self.cases.items():
            for c, n in v.items():
                if len(n) != 1:
                    return False





