import pygame

vec = pygame.math.Vector2


class Ground(pygame.sprite.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((55,15,55))
        self.rect = self.image.get_rect()

        # Position and direction
        self.rect.move_ip(0, 600-h)