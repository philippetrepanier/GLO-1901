print("Console")
"""
    Deprecated, le contenu est maintenant directement dans la classe grille
"""
class Console:
    def __str__(self, reponse):
        count = 0
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2566" + \
              "\u2550" * 9 + "\u2557" + '\n'
        for l in Grille.lignes:
            liste = []
            for c in Grille.colonnes:
                liste.append(reponse[l][c])
            res += ' ' + l + ' \u2551 {0[0]}  {0[1]}  {0[2]} \u2551 {0[3]}  {0[4]}  {0[5]} \u2551 {0[6]}  {0[7]}  {0[8]} \u2551'.format(liste) + '\n'
            compte += 1
            if compte == 3 or count == 6:
                res += 3 * ' ' + "\u2560" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + "\u2563" + "\n"
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"
    print(res)
