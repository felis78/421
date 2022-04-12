from random import randint

#############################################################################

class Joueur:
	def __init__(self, nomJoueur):
		self.nomJoueur = nomJoueur


	def __get__nomDuJoueur(self):
		return self.nomJoueur 

	nom = property(__get__nomDuJoueur) #renvoie le nom de l'utilisateur lié a la fonction

	def JoueurGagnant(self, resultatJoueur):
		gagnant = [[4,2,1], [4,1,2], [2,1,4], [2,4,1], [1,2,4], [1,4,2]]
		for i in gagnant:
			if resultatJoueur in gagnant:
				return True

	def JoueursPerdants(self, resultatJoueur, joueursPerdants):
		print(f"les joueurs ")

#############################################################################

class Des: #renvoie une valeur aléatoire de 1 à 6 inclus ous forme d'un tableau
    def __init__(self):
        pass

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
        while self.cpt != NombreJoueurs:
            joueur=Joueur(self.messages(3, 0, 0, 0))
            self.tableau.append(joueur)
            self.cpt += 1
        self.lancementDes(self.tableau)


    def initialisation(self, choix):
        if choix == 1:
            nombreJoueurs=(self.messages(2, 0, 0, 0))
            self.creerJoueur(nombreJoueurs)


    def lancementDes(self, joueurs):
        self.messages
        des = Des()
        for i in joueurs:
            self.resultat = des.LancerDes()
            nomDuJoueur = Joueur.nom
        self.resultats(self.resultat, nomDuJoueur)


    def resultats(self,  resultat, nomDuJoueur):
        print (resultat, nomDuJoueur)
        gagnant = Joueur.JoueurGagnant(resultat)
        self.messages(5, 0, resultat, nomDuJoueur)
        

        if gagnant == True:
            self.messages(6,nomDuJoueur,0, 0)
            self.finDuJeu()

        elif gagnant == False:
            lancementDes()


    def finDuJeu(self):
        pass
    		

Jeu()