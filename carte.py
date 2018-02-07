import pygame
from pygame.locals import * 
from constantes import *

class Carte:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
    
    #genere la liste à afficher
    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    #affiche la map en fonction de la liste generer
    def afficher(self, fenetre):
        #on charge les images
        baseBleu = pygame.image.load(images/carreBleu.png).convert_alpha()
        baseRouge = pygame.image.load(images/carreRouge.png).convert_alpha()
        montagne = pygame.image.load(images/carreMarron.png).convert_alpha()
        prairie = pygame.image.load(images/carreVert.png).convert_alpha()
        eau = pygame.image.load(images/carreEau.png).convert_alpha()

        #on parcours la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #on parcours ligne par ligne
            num_case = 0


