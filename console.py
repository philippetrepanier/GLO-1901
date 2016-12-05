print("Console")

class Console:
    def __init__(self):
        self.data ="PU"
    def afficherConsole(self, reponse):
        #On devrait splitter la liste en 9 liste
        verticale = ['A','B','C','D','E','F','G','H','I']
        listeligne = reponse.split(9)
        res = '   123 456 789'\n'  +---+---+---+'
        for ligne in listeligne:
            res += Verticale[ligne] + ' |'
            for nombre in ligne:
                res += '|' + ligne[nombre]
        res += '+---+---+---+'

class Console:
    def __init__(self,reponse):
        self.reponse[l][c] #???
    def __str__(self, reponse):
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2557" + '\n'
        for l in Grille.lignes:
            for c in Grille.colonnes:
                res += ' ' + c + ' \u2551 {}  {}  {} \u256C  {}  {}  {} \u256C {}  {}  {} \u2563'.format(reponse[l][c])
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"




