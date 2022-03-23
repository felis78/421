from random import randint

class Joueur():
	def __init__(self, nombreJoueurs):
		self.nombreJoueurs = nombreJoueurs

	def afficherNombreJoueurs(self):
		print("Vous serez ", self.nombreJoueurs, "joueurs")

	def Joueur_gagnant(self, resultatJoueur):
		gagnant = [[4,2,1], [4,1,2], [2,1,4], [2,4,1], [1,2,4], [1,4,2]]
		for i in gagnant:
			if resultatJoueur in gagnant:
				return True



class Des():
    def __init__(self):
    	pass

    def lancer_des(self):
    	score = []
    	for tableau in range (3):
        	valeur_de = randint(1, 6)
        	score.append(valeur_de)
            
    	return score


print("Binvenue sur le jeu du 421 \n Pour jouer tapez 1, Pour quitter tapez 2")
choix = input()
print (choix)
if choix == "1":
	print("Entrez le nombre de joueurs et definissez vous un numero")
	nombre_joueurs = input()
	joueurs = Joueur(nombre_joueurs)
	joueurs.afficherNombreJoueurs()
	
	print("1: lancer les dés 2: Quitter")
	choix = input()
	
	nombre_joueurs = int(nombre_joueurs)
	print(nombre_joueurs)
	relancer = 0
	while relancer != 2:
		joueur = 0
		for i in range(nombre_joueurs):
			joueur +=1
			des = Des()
			resultatJoueur = des.lancer_des()
			print(resultatJoueur)
			resultat = joueurs.Joueur_gagnant(resultatJoueur)
			print(resultat)
			if resultat == True:
				print("Le joueur", joueur, "a gagné.\n 1: relancer 2: Quitter" )
				relancer = input()
				if relancer == "2":
					exit()

		
		print("Pas de gagnant pour ce tour.\n 1: Relancer 2: Quitter")
		relancer = input()
		if relancer == "2":
			exit()

else:
	quit()






