import pygame
from pygame.locals import * 
from constantes import *

class Carte:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
    
    #genere la liste à afficher
    def generer(self): #on definit generer 
        with open(self.fichier, "r") as fichier: #pour ouvrir le fichier et le lire
            structure_niveau = [] #cree une liste 
            for ligne in fichier: #pour chaque ligne du ficher
                ligne_niveau = [] #on fait une liste 
                for sprite in ligne: #pour chaque lettre de chaque ligne 
                    if sprite != '\n':#si lettre != de '\n'= retour a la ligne 
                        ligne_niveau.append(sprite) #on rajoute lettre a la liste ligne niveau 
                structure_niveau.append(ligne_niveau) # on rajoutte les listes ligne niveau a la liste structure 
            self.structure = structure_niveau

    #affiche la map en fonction de la liste generer
    def afficher(self, fenetre):
        #on charge les images
        coffre = pygame.image.load(image_coffre).convert_alpha()
        depart = pygame.image.load(image_depart).convert_alpha()
        mur = pygame.image.load(image_mur).convert_alpha()
        #on parcours la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #on parcours ligne par ligne
            num_case = 0
            for sprite in ligne:
                #on calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'c':  #si lettre = c charger coffre             
                    fenetre.blit(coffre, (x,y))
                elif sprite == 'd':                 #d = depart
                    fenetre.blit(depart, (x,y))
                elif sprite == 'm':                 #m = mur
                    fenetre.blit(mur, (x,y))
                num_case += 1
            num_ligne += 1