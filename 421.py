from random import randint
from colorama import Fore, Back, Style, init, deinit

init()

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
        self.tableauresultats = []
        self.initialisation(self.messages(1, 0, 0 ,0))
        

  
    def messages(self, numberMessage, JoueurGagnant, resultatJoueur, nomDuJoueur):
        try:
            if numberMessage == 1:
                self.choix = int(input(Fore.RED + "############################\nBienvenue dans le Jeu du 421\n############################\n\n\n\nPour jouer tapez 1, pour quitter tapez 2\n"))
                return self.choix
                
            if numberMessage == 2:
                self.choix= int(input("Entrez le nombre de joueurs:\n "))
                return self.choix

            if numberMessage == 3:
                self.choix = (input("Entrez votre nom:\n "))
                return self.choix

            if numberMessage == 4:
                self.choix = int(input("1: lancer les dés \n2: Quitter\n"))
                return self.choix

            if numberMessage == 5:
               self.choix = print(f"le joueur {nomDuJoueur} a fait {resultatJoueur}\n")

            if numberMessage == 6:
                self.choix = print(f"\nLe joueur {nomDuJoueur} a gagné.\n" )

            if numberMessage == 7:
                self.choix = print("Pas de gagnant pour ce tour \n")

            if numberMessage == 8:
                self.choix = int(input("\n\n      #####      \nLe jeu est terminé.\n      #####      \n\n Si vous souhaitez rejouer tapez 1, sinon tapez 2\n"))

        except ValueError:
            print("Please read the text and type the value\n")
            Jeu()
        


    def creerJoueur(self, NombreJoueurs): #recupère le nombre de joueurs et demande d'entrer les noms pour initialiser le jeu
        while self.cpt != NombreJoueurs:
            self.joueur = self.messages(3, 0, 0, 0)
            self.tableau.append(self.joueur)
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
                    self.tableauresultats.append(self.resultat)
                self.resultats(self.tableauresultats, joueurs)

            if choix == 2:
                self.finDuJeu()


    def resultats(self,  resultat, nomDuJoueur):
        cpt = 0
        for resultatJoueur in resultat:
            self.messages(5, 0, resultatJoueur, nomDuJoueur[cpt])
            self.joueur=Joueur()
            gain = self.joueur.JoueurGagnant(resultatJoueur)
            if gain == True:
                self.messages(6, 0, 0, nomDuJoueur[cpt])
                self.finDuJeu()
            cpt+=1

        if gain == False:
            self.messages(7, 0, 0, 0)
            self.tableauresultats = []
            self.lancementDes(self.tableau)


    def finDuJeu(self):
        self.messages(8, 0, 0, 0)
        if self.choix == 1:
            self.tableauresultats = []
            self.lancementDes(self.tableau)

        else:
            print("\n###############    Merci d'avoir joué au 421, à bientôt !!!    ###############\n")
            deinit()
            quit()
    		

Jeu()