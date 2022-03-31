from random import randint

class Jeu:
	def __init__(self):
		print("Binvenue sur le jeu du 421 \n Pour jouer tapez 1, Pour quitter tapez 2")
		choix = input()
		demanderNombreJoueurs(choix)

	def lancerJeu(self, nombreJoueur):
		nombreJoueurs = int(nombre_joueurs)
		relancer = 0
		while relancer != 2:
			joueur = 0
			for i in range(nombreJoueurs):
				joueur +=1
				des = Des()
				resultatJoueur = des.lancer_des()
				print("Le joueur ", joueur, "a fait ",resultatJoueur)
				resultat = joueurs.Joueur_gagnant(resultatJoueur)
				if resultat == True:
					print("Le joueur", joueur, "a gagné.\n 1: relancer 2: Quitter" )
					relancer = input()
				if relancer == "2":
					exit()

	def demanderNombreJoueurs(self, choix):
		if choix == 1:
			print("Entrez le nombre de joueurs et definissez vous un numero")
			nombre_joueurs = input()
			joueurs = Joueur(nombre_joueurs)
			joueurs.afficherNombreJoueurs()


		print("Pas de gagnant pour ce tour.\n 1: Relancer 2: Quitter")
		relancer = input()
		if relancer == "2":
			exit()


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
		

class Des:
    def __init__(self):
    	pass

    def lancer_des(self):
    	score = []
    	for tableau in range (3):
        	valeur_de = randint(1, 6)
        	score.append(valeur_de)
            
    	return score






	print("1: lancer les dés 2: Quitter")
	choix = input()
	if choix.isdigit():
		if choix != 1 or choix != 2:
			print:("Not 1 or 2")
			quit()

		else:
			lancerJeu(nombre_joueurs)
			

	else:
		print("On avait dit un NOMBRE de joueurs")
		quit()
	
	

else:
	quit()






