import pygame

class Player():
    def __init__(self,ground):

        # Position and direction
        self.pos = [340, 240]
        self.vel = [0,0]
        self.gravityConst = 0.5
        self.isJumping = False
        self.jumpHeight = -10
        self.ground = ground
        self.velWalk = 6
        self.wall = []
        self.image = pygame.Surface((70, 70))
        self.image.fill((55,55,55))
        self.rect = self.image.get_rect()

    def run(self):
        if self.isJumping :
            print(self.vel)
            if self.vel[1] < self.jumpHeight:
                self.vel[1] = 0
                self.isJumping = False
            else:
                self.vel[1]-=0.5
        self.gravity()
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.midbottom = self.pos

    def gravity(self):
        if not self.ground.rect.colliderect(self.rect) :
            self.pos[1] += self.gravityConst
        

    def jump(self):    
        if not self.isJumping:
            print('jumping')
            self.isJumping = True
    def left(self):
        for rec in self.wall:
            if rec.rect.colliderect(self.rect):
                return 0
        self.pos[0] += -self.velWalk
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.midbottom = self.pos

    def right(self):
        for rec in self.wall:
            if rec.rect.colliderect(self.rect):
                return 0
        self.pos[0] += self.velWalk
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.midbottom = self.pos
