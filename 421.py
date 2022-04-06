from random import randint

class Joueur:
	def __init__(self, nombreJoueurs):
			self.nombreJoueurs = nombreJoueurs

	def afficherNombreJoueurs(self):
		print("Vous serez ", self.nombreJoueurs, "joueurs")

	def Joueur_gagnant(self, resultatJoueur):
		gagnant = [[4,2,1], [4,1,2], [2,1,4], [2,4,1], [1,2,4], [1,4,2]]
		for i in gagnant:
			if resultatJoueur in gagnant:
				return True

class Des:
    def __init__(self):
    	pass

    def lancer_des(self):
    	score = []
    	for tableau in range (3):
        	valeur_de = randint(1, 6)
        	score.append(valeur_de)
            
    	return score

class Jeu:

	def __init__(self):	
		self.nombreDeTours = 0
		test = False
		while test == False:
			try:
				choix = int(input("Binvenue sur le jeu du 421 \n Pour jouer tapez 1, Pour quitter tapez 2 "))
				test = True
			except ValueError:
				print("OOOOPS this is not integrer" )


		if choix == 1:
			test = False
			while test == False:
				try:
					nombre_joueurs = int(input("Entrez le nombre de joueurs et definissez vous un numero "))
					test = True
				except ValueError:
					print("OOOPS this is not integrer")
			
			joueurs = Joueur(nombre_joueurs)
			joueurs.afficherNombreJoueurs()
			
			test = False
			while test == False:
				try:
					choix = input(int("1: lancer les dés 2: Quitter "))
					test = True
				except ValueError:
					print("OOOPS, this is not integrer")
					
					
			if choix == 1:
				self.jeu(nombre_joueurs)

			else:
				quit()

		else:
			quit()

	def jeu(self, nombreJoueur):
		nombre_Joueurs = int(nombreJoueur)
		relancer = 0
		while relancer != 2:
			joueur = 0
			for i in range(nombre_Joueurs):
				joueur += 1
				des = Des()
				resultat_Joueur = des.lancer_des()
				print("Le joueur ", joueur, "a fait ",resultat_Joueur)
				joueurs = Joueur
				resultat = joueurs.Joueur_gagnant(0, resultat_Joueur)

				if resultat == True:
					test = False
					while test == False:
						try:
							relancer = input(int("Le joueur", joueur, "a gagné.\n 1: relancer 2: Quitter" ))
							test = True
						except ValueError:
							print("OOOPS this is not integrer")

					if relancer =="1":
						self.nombreDeTours += 1
						print(self.nombreDeTours)
					if relancer == "2":
						self.finDuJeu(self.nombreDeTours)
						exit()

			test = False
			while test == False:
				try:
					relancer = input(int("Pas de gagnant pour ce tour.\n 1: Relancer 2: Quitter"))
					test = True
				except ValueError:
					print ("OOOPS this is not integrer, try again")
			if relancer == "2":
				exit()

	
	def finDuJeu(self, nombreDeTours):
		print(f"Le jeu est terminé, voici les scores {nombreDeTours}")
Jeu()




