import pygame

#Initialisation de pygame
pygame.init()

#Création d'une fenetre de la taille de l'ecran redimensionnable
ecran = pygame.display.set_mode((1250, 700))

pygame.display.set_caption("Projet Python Enzo et Hugo !")

continuer = True

while continuer:
    #On crée un rectangle rose
    pygame.draw.rect(ecran, (225,0,0), (0, 00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (500,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (562.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (625,00, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (687.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,00, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,00, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,00, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,00, 62.5,58.33))
    
    pygame.draw.rect(ecran, (225,0,0), (0, 58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5, 58.330, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (500,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (562.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (625,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (687.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125,58.33, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,58.33, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (500,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (562.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (625,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (687.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,0116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,116.66, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,116.66, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5, 174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (500,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (562.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (625,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (687.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125,174.99, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,174.99, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0, 233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (500,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (562.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (625,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (687.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,233.32, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,233.32, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5,  291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (500, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (562.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (625, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (687.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125, 291.65, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5, 291.65, 62.5,58.33))
       
    pygame.draw.rect(ecran, (225,0,0), (0,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (500,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (562.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (625,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (687.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,349.98, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,349.98, 62.5,58.33))
    
    pygame.draw.rect(ecran, (225,0,0), (0, 408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5, 408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (500,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (562.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (625,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (687.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125,408.31, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,408.31, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (500,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (562.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (625,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (687.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,466.64, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,466.64, 62.5,58.33))
    
    pygame.draw.rect(ecran, (225,0,0), (0, 524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5, 524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (500,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (0, 255, 255), (562.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (625,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (687.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125,524.97, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,524.97, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0, 583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (62.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (125,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (187.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (250,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (312.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (375,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (437.5, 583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (500,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (562.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (625,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (687.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (750,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (812.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (875,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (937.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1000,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1062.5,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1125,583.3, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,583.3, 62.5,58.33))

    pygame.draw.rect(ecran, (225,0,0), (0,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (62.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (125,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (187.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (250,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (312.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (375,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (437.5, 641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (500,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (158, 99, 35), (562.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (625,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (687.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (750,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (812.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (875,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (937.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1000,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (119, 245, 5), (1062.5,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (107, 219, 4), (1125,641.63, 62.5,58.33))
    pygame.draw.rect(ecran, (15, 5, 107), (1187.5,641.63, 62.5,58.33))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    #Actulisation pour afficher le rectangle rose
    pygame.display.flip()
pygame.quit()