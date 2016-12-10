"""
    Ce fichier est responsable de la résolution du sudoku par backtracking
"""
__auteur__ = "IDUL"
__date__ = "2016-12-09"
__coequipiers__ = "IDUL", "IDUL"

import itertools
from copy import deepcopy


class Grille:
    """
        Classe grille qui est responsable des opérations sur la grille et du stockage des valeurs
    """
    def __init__(self, lignesfichier):
        """
            Lors de l'initialisation d'un objet Grille les données sont mises en mémoire
            sous forme de dictionnaire afin de pouvoir les manipuler plus facilement
        :param lignesfichier: Lignes du fichier sources (longueur maxi de 81 char)
        """
        # Définitions de concepts généraux
        self.colonnes = "123456789"
        self.lignes = "ABCDEFGHI"
        self.cases = {}
        l3 = ["ABC", "DEF", "GHI"]
        c3 = ["123", "456", "789"]
        self.carrés = list(itertools.product(l3, c3))

        compte = 0
        for l in self.lignes:
            self.cases[l] = {}
            for c in self.colonnes:
                if lignesfichier[compte] == "." or lignesfichier[compte] == "0":
                    self.cases[l][c] = self.colonnes
                else:
                    self.cases[l][c] = lignesfichier[compte]
                compte += 1
        self.cases = self.reduire()

    def __str__(self):
        """
            La fonction permet de faire un print(objet) afin d'afficher la grille en console
        :return: permet de retourner une grille avec mise en page
        """
        compte = 0
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + \
              "\u2566" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2557" + '\n'
        for l in self.lignes:
            liste = []
            for c in self.colonnes:
                liste.append(self.cases[l][c])
            res += ' ' + l + ' \u2551 {0[0]}  {0[1]}  {0[2]} \u2551 {0[3]}  {0[4]}  {0[5]} \u2551 {0[6]}  {0[7]}  {0[8]} \u2551'.format(
                liste) + '\n'
            compte += 1
            if compte == 3 or compte == 6:
                res += 3 * ' ' + "\u2560" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + \
                       "\u256C" + "\u2550" * 9 + "\u2563" + "\n"
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"
        return res

    def reduire(self, grilleréduite=None):
        """
            Fonction qui réduit les possibilités de la grille en prenant en considération
            les valeurs qui sont exactes et qui ont une seule place possible.
        :return: Retourne False si des conditions de la grille ne sont respectées
        """
        if grilleréduite is None:
            grilleréduite = deepcopy(self.cases)
        if grilleréduite is False:
            return False
        for l, v in grilleréduite.items():
            for c, n in v.items():
                if len(n) == 1:
                    for l2 in self.lignes:
                        if l2 != l:
                            if grilleréduite[l][c] == grilleréduite[l2][c]:
                                return False
                            else:
                                grilleréduite[l2][c] = grilleréduite[l2][c].replace(str(grilleréduite[l][c]), '')
                    for c2 in self.colonnes:
                        if c2 != c:
                            if grilleréduite[l][c] == grilleréduite[l][c2]:
                                return False
                            else:
                                grilleréduite[l][c2] = grilleréduite[l][c2].replace(str(grilleréduite[l][c]), '')
                    for l3, c3 in self.carrés:
                        if c in c3 and l in l3:
                            for l4 in l3:
                                for c4 in c3:
                                    if l4 != l and c4 != c:
                                        if grilleréduite[l][c] == grilleréduite[l4][c4]:
                                            return False
                                        else:
                                            grilleréduite[l4][c4] = grilleréduite[l4][c4].replace(
                                                str(grilleréduite[l][c]), '')
                else:
                    continue
        return grilleréduite

    def reduire2(self, grilleréduite=None):
        """
            Fonction qui fixe les valeurs dans les carrés dont la possibilité est certaine
        """
        if grilleréduite is None:
            grilleréduite = deepcopy(self.cases)
        if grilleréduite is False:
            return False
        for ligne, colonne in self.carrés:
            for num in self.colonnes:
                compte = 0
                lo = 'Z'
                co = '0'
                for l in ligne:
                    for c in colonne:
                        n = grilleréduite[l][c]
                        if num in n:
                            compte += 1
                            co = c
                            lo = l
                        else:
                            continue
                if compte == 1:
                    grilleréduite[lo][co] = str(num)
        return grilleréduite

    def recherche(self, grille=None):
        if grille is None:
            grille = self.cases
        if grille is False:
            return False
        if self.resolu(grille):
            self.cases = grille
            return True
        compte = 0
        for l, v in grille.items():
            for c, n in v.items():
                compte += len(n)
        if compte == 81:
            return False
        (elem, minimumligne, minimumcol) = self.minimum(grille)
        for num in elem:
            griller = deepcopy(grille)
            griller[minimumligne][minimumcol] = str(num)
            self.recherche(self.reduire2(self.reduire(griller)))

    def minimum(self, grille=None):
        if grille is None:
            grille = self.cases
        if grille is False:
            return False
        minimumligne = "0"
        minimumcol = "Z"
        lenmini = 9
        for l, v in grille.items():
            for c, n in v.items():
                if lenmini > len(n) > 1:
                    lenmini = len(n)
                    minimumcol = c
                    minimumligne = l
        return grille[minimumligne][minimumcol], minimumligne, minimumcol

    def resolu(self, grille=None):
        """
            Permet de vérifier si toute la grille contient un élément et qu'il est différent
            pour chaque colonne.
            La vérification est faite avec une somme vérifiant l'unicité de la solution.

            Il faut implanter une vérification similaire en carrés
        :return: Retourne False si il y a contradiction, sinon True
        """
        if grille is None:
            grille = self.cases
        if grille is False:
            return False
        for l, v in grille.items():
            verifligne = 0
            for c, n in v.items():
                if len(n) != 1:
                    return False
                else:
                    verifligne += 2 ** (int(n) - 1)
            if verifligne != 511:
                return False
        for c2 in self.colonnes:
            verifcol = 0
            for l2 in self.lignes:
                n = grille[l2][c2]
                if len(n) != 1:
                    return False
                else:
                    verifcol += 2 ** (int(n) - 1)
            if verifcol != 511:
                return False
        return True

