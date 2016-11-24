print("Lecture")

#Lecture du fichier
class Fichier:
    def __init__(self, fichiergrille):
        self.lignesfichier =''
        for i in fichiergrille:
            self.lignesfichier += ''.join(i).strip()
        self.lignesfichier = self.lignesfichier.replace(' ', '')

    def lire(self):
        print(self.lignesfichier)