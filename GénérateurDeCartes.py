#by judi_Co
__author__ = "judi_Co"
Version = 1

import random

#==========================================
#dictionnaire des carte
#cards dictionary
Carte = {
	"As": ["As", 14], 
	"2": ["2", 2], 
	"3": ["3", 3], 
	"4": ["4", 4], 
	"5": ["5", 5], 
	"6": ["6", 6], 
	"7": ["7", 7], 
	"8": ["8", 8], 
	"9": ["9", 9], 
	"10": ["10", 10], 
	"Valet": ["Valet", 11], 
	"Dame": ["Dame", 12], 
	"Roi": ["Roi", 13]
}

Liste0 = {"Jokers": "Jokers", "Jokers": "Jokers"}

#==========================================
#initialisation des liste de carte
#cards liste init
def piocheCartedictionnaire(Carte=Carte):
	Piques = {}
	for cle, Valeur in Carte.items():
		Piques[f"{cle} de Piques"] = Valeur

	Carreaux = {}
	for cle, Valeur in Carte.items():
		Carreaux[f"{cle} de Carreaux"] = Valeur

	Coeurs = {}
	for cle, Valeur in Carte.items():
		Coeurs[f"{cle} de Coeurs"] = Valeur

	Tréfles = {}
	for cle, Valeur in Carte.items():
		Tréfles[f"{cle} de Tréfles"] = Valeur


	#==========================================
	#Pile de cartes
	#Stack of cards
	Pile = {}

	Pile.update(Piques)
	Pile.update(Carreaux)
	Pile.update(Coeurs)
	Pile.update(Tréfles)

	#==========================================
	#mélanger la pile de carte
	#shuffle cards
	Keys = list(Pile.keys())
	random.shuffle(Keys)
	pioche = {}
	for key in Keys:
		pioche.update({key:Pile[key]})
	return pioche

#==========================================
#afficher les carte
#cards display
def printCarteListe(pioche=piocheCartedictionnaire()):
	for cle in pioche.keys():
		Cles = list(pioche)
	return Cles

#==========================================
#afficher les cartes
#cards display
#Liste = printCarteListe()
#Liste = piocheCartedictionnaire()

#afficher les cartes sous forme de Liste
#display maps in List form
print(printCarteListe())

#afficher les cartes sous forme de dictionnaire
#display maps in dictionary form
print(piocheCartedictionnaire())

#==========================================
