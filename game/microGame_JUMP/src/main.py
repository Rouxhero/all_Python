import pygame
import player
import ground

ground = ground.Ground(800,70)
player = player.Player(ground);


pygame.init()
pygame.font.init()

surface = pygame.display.set_mode((800, 600))

pygame.key.set_repeat(400, 30)

continu = True
while continu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = True
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_RIGHT:
                player.right()

    surface.fill((0,0,0))
    player.run()
    surface.blit(player.image, player.rect)
    surface.blit(ground.image, ground.rect)
    pygame.display.update()