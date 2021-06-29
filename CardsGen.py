#by judi_Co
author = "judi_Co"
Version = "1.2"

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

jokersCarte = {"Jokers1": ["Jokers", 15], "Jokers2": ["Jokers", 15]}

#==========================================
#initialisation des liste de carte
#cards liste init
def piocheD(jokers=False, Carte=Carte):
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
    if jokers == True:
        Pile.update(jokersCarte)

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
def piocheL(jocker=False, pioche = piocheD()):
    if jocker == True:
        pioche = piocheD(True)
    for cle in pioche.keys():
        Cles = list(pioche)
    return Cles

#===============================
def piocheLD(jocker=False,pioche=piocheD()):
    if jocker == True:
        pioche = piocheD(True)
    D = pioche
    for L in pioche.keys():
        L = list(pioche)

    return L, D

#==========================================
#ajouter True en variable dans les apelle de fonction pour ajouter les jocker 
#add True in var for add jocker

#stocker les cartes
#stock cards
#Liste = piocheL()
#Liste = piocheL(True)
#dictionnaire = piocheD()
#dictionnaire = piocheD(True)

#afficher les cartes sous forme de Liste
#display maps in List form
#print(piocheL())
#print(piocheL(True))

#afficher les cartes sous forme de dictionnaire
#display maps in dictionary form
#print(piocheD())
#print(piocheD(True))

#piocheLD() retourn en une liste et un dictionaire idantique
#print(piocheDl())     #no arg = liste and dic
#print(piocheLD()[0]) #[0]= Liste
#print(piocheLD()[1]) #[1]= dictionaire
#print(piocheLD(True)) #no arg and True= liste, dic and jocker
#print(piocheLD(True)[0]) #[0] and True= liste and jocker
#print(piocheLD(True)[1]) #[1] and True= dictionaire and jocker

#==========================================
