import pygame
from pygame.locals import *
from carte import *
from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre)) #fonction pour cree une fenetre

icone = pygame.image.load(image_icone) #icone du jeu chargé
pygame.display.set_icon(icone) #afficher
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPAL
continuer = 1
while continuer: #boucle qui tourne tant que continuer =1
    #chargement page accueil
    accueil = pygame.image.load(image_accueil).convert() #charger image accueil
    fenetre.blit(accueil, (0,0)) # 0,0= prendre la taille de la fenetre 

    pygame.display.flip()#mettre a jour pour afficher l'image 

    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE ACCUEIL
    while continuer_accueil:
        #limite vitesse de la boucle pour la ram
        pygame.time.Clock().tick(30) #permet de pas laguer

        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables continuer a 0
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer.accueil = 0
                continuer_jeu = 0
                continuer = 0

                choix = 0
            elif event.type == KEYDOWN: #sinon evenement clavier
                if event.key == K_F1: #f1
                    continuer_accueil = 0  #On quitte l'accueil
                    choix = 'n1' #choix lvl 1
    
    if choix != 0: # different de 0
        fond = pygame.image.load(image_fond).convert() #charger l'image de fond 
        
        carte = Carte(choix) # on recupere n1
        carte.generer()
        carte.afficher(fenetre)

        guerrier = Perso("images/Droite ISN.png","images/Gauche ISN.png","images/Face ISN.png","images/Dos ISN.png",carte)
        
    #BOUCLE JEU
    while continuer_jeu:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

           
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            
            elif event.type == KEYDOWN:
               
                if event.key == K_ESCAPE:
                    continuer_jeu = 0 # 

                if event.key == K_RIGHT:
                    guerrier.deplacer('droite')

                if event.key == K_LEFT:
                    guerrier.deplacer('gauche')

                if event.key == K_UP:
                    guerrier.deplacer('haut')
                
                if event.key == K_DOWN:
                    guerrier.deplacer('bas')
        
                    
        fenetre.blit(fond, (0,0)) 
        carte.afficher(fenetre)
        fenetre.blit(guerrier.direction, (guerrier.x, guerrier.y))
        pygame.display.flip()