# Ce fichier est responsable de la résolution du sudoku par backtracking
#petite fleur sèche
print("Solver")


class Grille:
    def __init__(self, lignesfichier):
        # Définitions de concepts généraux
        self.colonnes = "123456789"
        self.lignes = "ABCDEFGHI"
        self.cases = {}

        compte = 0
        for l in self.lignes:
            self.cases[l] = {}
            for c in self.colonnes:
                if lignesfichier[compte] == "." or lignesfichier[compte] == "0":
                    self.cases[l][c] = self.colonnes
                else:
                    self.cases[l][c] = lignesfichier[compte]
                compte += 1

        self.reduire()

    def reduire(self):
        grille_réduite = {}
        for l, v in self.cases.items():
            grille_réduite[l] = {}
            for c, n in v.items():
                if len(n) == 1:
                    for l2 in self.lignes:
                        if l2 != l:
                            if self.cases[l][c] == self.cases[l2][c]:
                                return False
                            else:
                                grille_réduite[l2][c] =
                                print(self.cases[l][c], self.cases[l2][c])


                else:
                    continue


                            #self.cases[l][c] = self.cases[l][c].replace(str(self.cases[l2][c]), 'pou')
                            #print('POURR')

                    # for carrés'''


    # Permet de vérifier si toute la grille contient un élément
    def resolu(self):
        for l, v in self.cases.items():
            for c, n in v.items():
                if len(n) != 1:
                    return False





