from random import randint

#############################################################################

class Joueur:
    def JoueurGagnant(self, resultatJoueur):
        gagnant = [[4,2,1], [4,1,2], [2,1,4], [2,4,1], [1,2,4], [1,4,2]]
        for i in gagnant:
            if resultatJoueur in gagnant:
                return True

            else:
                return False

    def JoueursPerdants(self, resultatJoueur, joueursPerdants):
        print(f"les joueurs ")

#############################################################################

class Des: #renvoie une valeur aléatoire de 1 à 6 inclus ous forme d'un tableau

    def LancerDes(self):
        score = []
        for tableau in range (3):
            valeur_de = randint(1, 6)
            score.append(valeur_de) 
        return score 

##############################################################################

class Jeu:
    def __init__(self):
        self.nombreDeTours = 0
        self.cpt = 0
        self.choix = 0
        self.tableau = []
        self.resultat = 0
        self.joueur = 0
        self.initialisation(self.messages(1, 0, 0 ,0))

  
    def messages(self, numberMessage, JoueurGagnant, resultatJoueur, nomDuJoueur):
        try:
            if numberMessage == 1:
                self.choix = int(input("Welcome on 421 \n To play type 1, To quit type 2 "))
                return self.choix
                
            if numberMessage == 2:
                self.choix= int(input("Entrez le nombre de joueurs: "))
                return self.choix

            if numberMessage == 3:
                self.choix = (input("Entrez votre nom: "))
                return self.choix

            if numberMessage == 4:
                self.choix = int(input("1: lancer les dés \n 2: Quitter"))
                return self.choix

            if numberMessage == 5:
               self.choix = (f"le joueur {nomDuJoueur} a fait {resultatJoueur}")

            if numberMessage == 6:
                self.choix = int(input(f"Le joueur{nomDuJoueur} a gagné." ))

            if numberMessage == 7:
                self;choix = int(input("Pas de gagnant pour ce tour \n 1: relancer 2: Quitter " ))

        except ValueError:
            print("Please read the text and type the value")


    def creerJoueur(self, NombreJoueurs): #recupère le nombre de joueurs et demande d'entrer les noms pour initialiser pour chaque jouer la classe joueur
        recupMessage = 0
        while self.cpt != NombreJoueurs:
            self.joueur = self.messages(3, 0, 0, 0)
            self.tableau.append(self.joueur)
            print(self.tableau)
            self.cpt += 1
        self.lancementDes(self.tableau)


    def initialisation(self, choix):
        if choix == 1:
            nombreJoueurs=(self.messages(2, 0, 0, 0))
            self.creerJoueur(nombreJoueurs)


    def lancementDes(self, joueurs):
            choix = self.messages(4, 0, 0, 0)
            if choix == 1:
                des = Des()
                for i in joueurs:
                    self.resultat = des.LancerDes()
                    nomDuJoueur = i
                self.resultats(self.resultat, nomDuJoueur)

            if choix == 2:
                self.finDuJeu()


    def resultats(self,  resultat, nomDuJoueur):
        self.joueur=Joueur()
        gain = self.joueur.JoueurGagnant(resultat)
        print(gain)
        self.messages(5, 0, resultat, nomDuJoueur)
        

        if gain == True:
            self.messages(6,nomDuJoueur,0, 0)
            self.finDuJeu()

        if gain == False:
            self.lancementDes(self.tableau)


    def finDuJeu(self):
        quit()
    		

Jeu()