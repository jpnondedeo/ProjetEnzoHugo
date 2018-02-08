import pygame
from pygame.locals import *
from carte import *
from constantes import *

pygame.init()

#Ouverture fenetre
fenetre = pygame.display.set_mode((cote_fenetre + 600, cote_fenetre + 120))

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPAL
continuer = 1
while continuer:
    #chargement page accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    pygame.display.flip()

    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE ACCUEIL
    while continuer_accueil:
        #limite vitesse de la boucle pour la ram
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer.accueil = 0
                continuer_jeu = 0
                continuer = 0

                choix = 0
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    continuer_accueil = 0  #On quitte l'accueil
                    choix = 'n1'
    
    if choix != 0:
        fond = pygame.image.load(image_fond).convert()
        #Génération de la carte 1
        carte = Carte(choix)
        carte.generer()
        carte.afficher(fenetre)
    
    #BOUCLE JEU
    while continuer_jeu:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #Si user quitte on met variable boucle jeu à 0 et la variable général à 0 pour fermer l'appli
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            
            elif event.type == KEYDOWN:
                #si user press echap il revient au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                    
        fenetre.blit(fond, (0,0))
        carte.afficher(fenetre)
        pygame.display.flip()