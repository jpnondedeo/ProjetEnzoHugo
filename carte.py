import pygame
from pygame.locals import * 
from constantes import *

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre)) #fonction pour cree une fenetre
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


class Perso:
    def __init__(self, droite, gauche, bas, haut, niveau):
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()

        self.caseX = 0 #position dans la grille 
        self.caseY = 0
        self.x = 0 #position en pixel
        self.y = 0

        self.direction = self.droite
        self.niveau = niveau

    def deplacer(self, direction):
        
        if direction == 'droite': #si direction = droite
            if self.caseX < nombre_sprite_cote-1:# et si position < 21
                if self.niveau.structure[self.caseY][self.caseX+1] !='m': #et si la case de destination n'est pas un mur
                    self.caseX = self.caseX + 1
                    self.x = self.x + taille_sprite
            self.direction = self.droite 

        if direction == 'gauche': #si direction = gauche
            if self.caseX > 0: # et si position > 0
                if self.niveau.structure[self.caseY][self.caseX-1] !='m': #et si la case de destination n'est pas un mur
                    self.caseX = self.caseX - 1
                    self.x = self.x - taille_sprite
            self.direction = self.gauche 

        if direction == 'bas': #si direction = bas
            if self.caseY < nombre_sprite_cote-1: # et si position < 21
                if self.niveau.structure[self.caseY+1][self.caseX] !='m': #et si la case de destination n'est pas un mur
                    self.caseY = self.caseY + 1
                    self.y = self.y + taille_sprite
            self.direction = self.bas 
            
                        
        if direction == 'haut': #si direction = haut
            if self.caseY > 0: # et si position >0
                if self.niveau.structure[self.caseY-1][self.caseX] !='m': #et si la case de destination n'est pas un mur
                    self.caseY = self.caseY - 1
                    self.y = self.y - taille_sprite
            self.direction = self.haut
        
        if self.caseX == 21 and self.caseY == 21 :
            fin = pygame.image.load(image_fin).convert_alpha #icone du jeu chargé
            pygame.display.set_icon(fin) 
        
            
         