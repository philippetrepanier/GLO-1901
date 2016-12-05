# Fichier qui permet de faire l'affichage graphique de l'utilisateur
# Il est importé dans sudoku.py
from tkinter import *

base = Tk()
base.title('Sudoku')
sudoku = [[0 for x in range(9)]for x in range(9)]
Boutton = [[1 for x in range(10)]for x in range (10)]
def CouleurSudoku(i,j):
    C=(3*int((i-1)/3)) + int((j-1)/3) + 1
    if C%2==0:
        C='green'
    else:
        C='blue'
    return C

frame = Frame(base)
frame.grid(ipady=1,ipadx=1)

for i in range(1,10):
    for j in range(1,10):
        Boutton[i][j] = Button(frame, width=2)
        Boutton[i][j].grid(row=i,column=j,padx=3, pady=2)
        Boutton[i][j].configure(bg=CouleurSudoku(i,j))
base.mainloop()

