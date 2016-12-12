# Fichier qui permet de faire l'affichage graphique de l'utilisateur
# Il est importé dans sudoku.py
from tkinter import *
from tkinter.messagebox import *


root = Tk()
root.title('Sudoku')
Entrée = [[1 for x in range(10)]for x in range (10)]

def CouleurSudoku(i,j):
    C=(3*int((i-1)/3)) + int((j-1)/3) + 1
    if C%2==0:
        C='grey'
    else:
        C='black'
    return C

frame = Frame(root)
frame.grid(ipady=0,ipadx=0)

ListeValide = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def alert():
    k=Entrée[i][j]
    if Entrée[i][j] in ListeValide==True:
        return k
    else:
        return showerror("Valeur non-valide","Veuillez entrer une valeur valide")

for i in range(1,10):
    for j in range(1,10):
        Entrée[i][j] = Entry(frame, width=1, bg=CouleurSudoku(i,j), fg="white")
        Entrée[i][j].grid(row=i,column=j)
root.mainloop()

