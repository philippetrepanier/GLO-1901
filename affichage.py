"""
    Fichier responsable de l'affichage graphique
"""
__auteur__ = "CETRE83"
__date__ = "2016-12-09"
__coequipiers__ = "JEROY154", "PHTRE60"
from tkinter import *


class Affichage:
    """
        Classe Affichage graphique
    """

    def __init__(self, grille):
        self.cases = grille
        self.root = Tk()
        self.root.title('Sudoku')
        self.root.resizable(width=False, height=False)

        self.BarreMenu = Menu(self.root)
        self.root.config(menu=self.BarreMenu)
        self.editmenu = Menu(self.BarreMenu, tearoff=0)
        frame = Frame(self.root)
        frame.grid(ipady=0, ipadx=0)
        ListeValide = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Liste qui permettra de vérifier la validité du charactère entré dans une case
        for i in range(0, 9):
            for j in range(0, 9):
                cases = Label(frame, width=3, height=2, bg=self.couleur_sudoku(i, j), fg="Black",
                              relief=self.texturecase(i, j), font=("Times", 15), text=self.texte(i, j))
                cases.grid(row=i, column=j)

        self.root.mainloop()

    def couleur_sudoku(self, i, j):
        """
            Fonction qui retourne l'emplacement de la case dans la grille
            une couleur afin de créer une séparation de 9 carrés de dimension 3x3
        """
        couleur = ""
        if 2 < i < 6 and 2 < j < 6:
            couleur += "white"
        elif 2 < i < 6:
            couleur += "grey"
        elif 2 < j < 6:
            couleur += "grey"
        else:
            couleur += "white"
        return couleur

    def texturecase(self, i, j):
        """
            Fonction qui selon l'emplacement de la case dans la grille, retourne un relief différent.
        """
        d = ""
        if (i + j) % 2 == 1:
            d += "sunken"
        else:
            d += "flat"
        return d

    def texte(self, i, j):
        i = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I'}.get(str(i))
        j += 1
        if len(self.cases[i][str(j)]) == 1:
            return self.cases[i][str(j)]
        else:
            return " "
