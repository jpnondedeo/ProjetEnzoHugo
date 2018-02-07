import pygame
from pygame.locals import *
from carte import *
from constantes import *

pygame.init()

#Ouverture fenetre
fenetre = pygame.display.set.mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)