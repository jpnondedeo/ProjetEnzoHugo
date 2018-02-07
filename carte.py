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
        baseBleu = pygame.image.load(image_bleu).convert_alpha()
        baseRouge = pygame.image.load(image_rouge).convert_alpha()
        pont = pygame.image.load(image_marron).convert_alpha()
        prairie = pygame.image.load(image_vert).convert_alpha()
        eau = pygame.image.load(image_eau).convert_alpha()

        #on parcours la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #on parcours ligne par ligne
            num_case = 0
            for sprite in ligne:
                #on calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'b':                   #b = carreBleu
                    fenetre.blit(baseBleu, (x,y))
                elif sprite == 'r':                 #r = carreRouge
                    fenetre.blit(baseRouge, (x,y))
                elif sprite == 'm':                 #m = carreMarron
                    fenetre.blit(pont, (x,y))
                elif sprite == 'v':                 #v = carreVert
                    fenetre.blit(prairie, (x,y))
                elif sprite == 'e':                 #e = carreEau
                    fenetre.blit(eau, (x,y))
                num_case += 1
            num_ligne += 1