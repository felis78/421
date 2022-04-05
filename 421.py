from random import randint

class Jeu:
	def __init__(self):
		print("Binvenue sur le jeu du 421 \n Pour jouer tapez 1, Pour quitter tapez 2")
		choix = input()
		self.demanderNombreJoueurs()

	def lancerJeu(self, nombreDeJoueurs):
		print(nombreDeJoueurs)
		relancer = 0
		while relancer != 2:
			joueur = 0
			for i in range(nombreDeJoueurs):
				joueur +=1
				resultatJoueur = self.Des()
				print("Le joueur ", joueur, "a fait ",resultatJoueur)
				resultat = self.Joueur_gagnant(resultatJoueur)
				if resultat == True:
					print("Le joueur", joueur, "a gagné.\n 1: relancer 2: Quitter" )
					relancer = input()
					if relancer == "2":
						exit()

				else:
					print("Pas de gagnant pour ce tour.\n 1: Relancer 2: Quitter")
					relancer = input()
					if relancer == "2":
						exit()

	def demanderNombreJoueurs(self):
		print("Entrez le nombre de joueurs et definissez vous un numero")
		nombre_joueurs = input()
		joueurs = Joueur(nombre_joueurs)
		joueurs.afficherNombreJoueurs()


class Joueur(Jeu):
	def __init__(self, nombre_Joueurs):
		self.nombreJoueurs = nombre_Joueurs

	def afficherNombreJoueurs(self):
		print("Vous serez ", self.nombre_Joueurs, "joueurs")
		nombreJoueurs = int(nombre_Joueurs)
		self.lancerJeu(nombreJoueurs)

	def Joueur_gagnant(self, resultatJoueur):
		gagnant = [[4,2,1], [4,1,2], [2,1,4], [2,4,1], [1,2,4], [1,4,2]]
		for i in gagnant:
			if resultatJoueur in gagnant:
				return True

	def renseignerJoueurs(self, nombreJoueurs):
		Joueurs = []
		cpt = 0
		while cpt != nombre_joueurs:
			print(f"Joueur{cpt+1} entrez votre nom")
			nom = input()
			if nom.isdigit():
				print("Ce n'est pas un nom, c'est un nombre")

			else:
				for c in Joueurs:
					if choix in Joueurs:
						print("Nom Déja entré")
					else:
						Joueurs.append()
						cpt += 1

		return Joueurs
		

class Des(Jeu):
	def __init__ (self):
		score = []
		for tableau in range(3):
			valeur_de = randint(1, 6)
			score.append(valeur_de)
            
		return score


Jeu()





