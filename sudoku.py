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

parser = argparse.ArgumentParser(
    description=("Sudoku pythonesque! Ce programme permet de résoudre des Sudokus. "
                 "Les options utiles sont les suivantes:")
)
parser.add_argument("-m", "--mode", choices=['manuel', 'automatique'], default='manuel',
                    help=("Choix du mode: En mode manuel l'utilisateur entre les valeurs du Sudoku. "
                          "En mode automatique le programme génère la solution. "))
parser.add_argument("-a", "--affichage", choices=['textuel', 'graphique'], default='textuel',
                    help=("Choix du mode: En mode textuel l'utilisateur intéragit directement "
                          "avec la console. En mode graphique un affichage permet de visualiser "
                          "la grille de Sudoku"))
parser.add_argument("fichier", type=argparse.FileType('r'))

# args = parser.parse_args(["testies.txt"])
args = parser.parse_args()

lignesfichier = lecture.lecture_fichier(args.fichier.readlines())
print("Sudoku Pythonesque \n \n")

if args.mode == 'manuel' and args.affichage == 'textuel':
    start_time = time.time()
    grille = solver.Grille(lignesfichier[0:81])
    print("Grile originale \n \n " + str(grille))
    grille.entrée(grille.cases)

if args.mode == 'automatique' and args.affichage == 'textuel':
    for i in range(0, len(lignesfichier) - 81, 81):
        start_time = time.time()
        grille = solver.Grille(lignesfichier[i:i + 81])
        print("Grile originale \n \n" + str(grille))
        grille.cases = grille.reduire(grille.reduire2(grille.reduire(grille.cases)))
        grille.recherche(grille.cases)
        print("\n Grille résolue")
        print(grille)
        print("Temps total d'exécution du programme : %.4f secondes \n" % (time.time() - start_time))
