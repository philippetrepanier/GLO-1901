print("Console")

class Console:
    def __str__(self, reponse):
        count = 0
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2566" + \
              "\u2550" * 9 + "\u2557" + '\n'
        for l in Grille.lignes:
            liste = []
            for c in Grille.colonnes:
                liste.append(reponse[l][c])
            res += ' ' + l + ' \u2551 {}  {}  {} \u256C  {}  {}  {} \u256C {}  {}  {} \u2563'.format(liste)
            count += 1
            if count == 3 or 6:
                res +='   \u2554" + " " * 9 + "\u256C" + " " * 9 + "\u256C" + " " * 9 + "\u2563" + "\n"'
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"
    print(res)

