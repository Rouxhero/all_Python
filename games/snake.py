import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
largeur, hauteur = 640, 480
taille_case = 20

# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
vert = (0, 255, 0)

# Création de l'écran
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")

# Fonction pour afficher le message de fin de jeu
def message_fin(texte):
    police = pygame.font.Font(None, 36)
    texte_surface = police.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (largeur // 2, hauteur // 2)
    ecran.blit(texte_surface, texte_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

# Fonction principale du jeu
def jouer():
    # Initialisation du serpent
    serpent = [(3, 1), (3, 2), (3, 3)]
    direction = (1, 0)

    # Position initiale de la pomme
    pomme = (random.randint(0, (largeur // taille_case) - 1), random.randint(0, (hauteur // taille_case) - 1))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (1, 0)

        # Déplacer le serpent
        tête = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])
        serpent.insert(0, tête)

        # Vérifier si le serpent mange la pomme
        if serpent[0] == pomme:
            pomme = (random.randint(0, (largeur // taille_case) - 1), random.randint(0, (hauteur // taille_case) - 1))
        else:
            serpent.pop()

        # Vérifier si le serpent a perdu
        if (serpent[0][0] < 0 or serpent[0][0] >= largeur // taille_case or
                serpent[0][1] < 0 or serpent[0][1] >= hauteur // taille_case or
                serpent[0] in serpent[1:]):
            message_fin("Game Over")
            jouer()

        # Effacer l'écran
        ecran.fill(noir)

        # Dessiner le serpent
        for segment in serpent:
            pygame.draw.rect(ecran, vert, (segment[0] * taille_case, segment[1] * taille_case, taille_case, taille_case))

        # Dessiner la pomme
        pygame.draw.rect(ecran, blanc, (pomme[0] * taille_case, pomme[1] * taille_case, taille_case, taille_case))

        # Mettre à jour l'écran
        pygame.display.flip()

        # Contrôler la vitesse du jeu
        pygame.time.Clock().tick(10)

# Lancer le jeu
jouer()
