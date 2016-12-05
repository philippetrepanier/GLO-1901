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
                                grille_réduite[l2][c] = self.cases[l2][c].replace(str(self.cases[l][c]), '')
                    for c2 in self.colonnes:
                        if c2 != c:
                            if self.cases[l][c] == self.cases[l][c2]:
                                return False
                            else:
                                grille_réduite[l][c2] = self.cases[l][c2].replace(str(self.cases[l][c]), '')
                else:
                    continue

        self.cases = grille_réduite

    def __str__(self):
        compte = 0
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2566" + \
              "\u2550" * 9 + "\u2557" + '\n'
        for l in self.lignes:
            liste = []
            for c in self.colonnes:
                liste.append(self.cases[l][c])
            res += ' ' + l + ' \u2551 {0[0]}  {0[1]}  {0[2]} \u2551 {0[3]}  {0[4]}  {0[5]} \u2551 {0[6]}  {0[7]}  {0[8]} \u2551'.format(liste) + '\n'
            compte += 1
            if compte == 3 or compte == 6:
                res += 3 * ' ' + "\u2560" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + "\u2563" + "\n"
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"
        return res


    # Permet de vérifier si toute la grille contient un élément
    def resolu(self):
        for l, v in self.cases.items():
            for c, n in v.items():
                if len(n) != 1:
                    return False





