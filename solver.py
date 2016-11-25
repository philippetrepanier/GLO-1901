# Ce fichier est responsable de la résolution du sudoku par backtracking
#petite fleur sèche
print("Solver")


class Grille:
    def __init__(self, lignesfichier):
        # Définitions de concepts généraux
        self.colonnes = "123456789"
        self.lignes = "ABCDEFGHI"
        self.nombres = self.colonnes
        self.cases ={}

        for l in self.lignes:
            compte = 0
            self.cases[l] = {}
            for c in self.colonnes:
                if lignesfichier[compte] == ".":
                    self.cases[l][c] = self.nombres
                else:
                    self.cases[l][c] = lignesfichier[compte]
                compte += 1

        self.reduire()

    def reduire(self):
        for l in self.lignes:
            for c in self.colonnes:
                c = str(c)
                if len(self.cases[l][c]) == 1:
                    continue
                else:
                    for l2 in self.lignes:
                        print(self.cases[l2][c])
                        print(l2, c)
                        if len(self.cases[l2][c]) == 1:
                            self.cases[l][c].replace(self.cases[l2][c], 'pou')
                            raise AssertionError
                    for c2 in self.colonnes:
                        if len(self.cases[l][c2]) == 1:
                            self.cases[l][c].replace(self.cases[l][c2], 'pou')
        print(self.cases)


