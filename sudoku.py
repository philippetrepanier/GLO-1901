import affichage
import solver
import lecture
import console
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--manuel", action="store_true", help="Mode manuel")
parser.add_argument("-a", "--automatique", action="store_true", help="Mode automatique")

args = parser.parse_args()

if args.manuel:
    print("Mode Manuel")
if args.automatique:
    print("Mode Automatique")
print("Sudoku Pythonesque")