import affichage
import solver
import lecture
import console
import argparse


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
print("Sudoku Pythonesque")

sudoku.imprimmer()
grille1 = solver.Grille(sudoku.lignesfichier)
print(grille1.cases)
