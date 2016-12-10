"""
    Fichier principal du projet Sudoku!
"""
__auteur__ = "IDUL"
__date__ = "2016-12-09"
__coequipiers__ = "IDUL", "IDUL"

import argparse
import time
import solver
import lecture

# import affichage



parser = argparse.ArgumentParser()
parser.add_argument("-m", "--manuel", action="store_true", help="Mode manuel")
parser.add_argument("-a", "--automatique", action="store_true", help="Mode automatique")
parser.add_argument("fichier", type=argparse.FileType('r'))

args = parser.parse_args(["testies.txt"])




sudoku = lecture.Fichier(args.fichier.readlines())

if args.manuel:
    print("Mode Manuel")
if args.automatique:
    print("Mode Automatique")
print("Sudoku Pythonesque \n \n")

start_time = time.time()
# sudoku.imprimmer()
grille1 = solver.Grille(sudoku.lignesfichier)
print("Grile originale \n \n " + str(grille1))

grille1.cases = grille1.reduire(grille1.reduire2(grille1.reduire(grille1.cases)))

print("Grille réduite \n \n" + str(grille1) + "\n \n")
grille1.recherche(grille1.cases)
print("Temps totales d'exécution du programme : %.4f secondes" % (time.time() - start_time))
print(('OK'))
print(grille1)

for l in grille1.lignes:
    for c in grille1.colonnes:
        print(grille1.cases[l][c], end="")



#print(grille1.resolu())
#print(grille1.cases)
