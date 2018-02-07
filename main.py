import pygame
from carre import Carre

#Initialisation de pygame
pygame.init()

#Création d'une fenetre de la taille de l'ecran redimensionnable
ecran = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

pygame.display.set_caption("Projet Python Enzo et Hugo !")

continuer = True

while continuer:
    #On crée un rectangle rose
    pygame.draw.rect(ecran, (180, 20, 150), (0, 0, 300, 200))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

    #Actulisation pour afficher le rectangle rose
    pygame.display.flip()
pygame.quit()