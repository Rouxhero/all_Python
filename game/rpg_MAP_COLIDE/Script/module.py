# coding: utf-8
import pygame


def inv_font_draw(txt):
    pygame.font.init()
    inv_font = pygame.font.Font("cubic.ttf", 20)
    text = inv_font.render(txt, False, (255, 255, 255))
    return text


def load_img():
    db_img = []
    for i in range(int(open("../img/count.l", "r").read())):
        db_img += [
            pygame.transform.scale(
                pygame.image.load("../img/" + str(i) + ".png"), (64, 64)
            )
        ]
    return db_img


def load_img_inv():
    db_img = []
    for i in range(int(open("../img/item/count.l", "r").read())):
        db_img += [
            pygame.transform.scale(
                pygame.image.load("../img/item/" + str(i) + ".png"), (64, 64)
            )
        ]
    return db_img


	
i = 1


class newplayer:
    def __init__(self, n):
        self.name = n

        self.img_idle_left1 = pygame.transform.scale(
            pygame.image.load("../img/player/0.png"), (64, 64)
        )
        self.img_idle_down1 = pygame.transform.scale(
            pygame.image.load("../img/player/1.png"), (64, 64)
        )
        self.img_idle_up1 = pygame.transform.scale(
            pygame.image.load("../img/player/2.png"), (64, 64)
        )
        self.img_idle_right1 = pygame.transform.scale(
            pygame.image.load("../img/player/3.png"), (64, 64)
        )

        self.img_idle_left2 = pygame.transform.scale(
            pygame.image.load("../img/player/4.png"), (64, 64)
        )
        self.img_idle_down2 = pygame.transform.scale(
            pygame.image.load("../img/player/5.png"), (64, 64)
        )
        self.img_idle_up2 = pygame.transform.scale(
            pygame.image.load("../img/player/6.png"), (64, 64)
        )
        self.img_idle_right2 = pygame.transform.scale(
            pygame.image.load("../img/player/7.png"), (64, 64)
        )

        self.img_idle_left3 = pygame.transform.scale(
            pygame.image.load("../img/player/8.png"), (64, 64)
        )
        self.img_idle_down3 = pygame.transform.scale(
            pygame.image.load("../img/player/9.png"), (64, 64)
        )
        self.img_idle_up3 = pygame.transform.scale(
            pygame.image.load("../img/player/10.png"), (64, 64)
        )
        self.img_idle_right3 = pygame.transform.scale(
            pygame.image.load("../img/player/11.png"), (64, 64)
        )
        self.c_l = 1
        self.c_r = 1
        self.c_u = 1
        self.c_d = 1
        self.img = self.img_idle_down1
        self.x = 84
        self.y = 74
        self.inv = [
            ("2", 100),
            ("3", 1),
            ("1", 1),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
            ("0", 0),
        ]

    def cases(self, x, y):
        return (self.x + x - 20) // 64, (self.y + y - 10) // 64

    def left(self):
        if self.c_l == 1:
            self.img = self.img_idle_left1
            self.x -= 16
            self.c_l += 1
            return 0
        if self.c_l == 2:
            self.img = self.img_idle_left2
            self.x -= 16
            self.c_l += 1
            return 0
        if self.c_l == 3:
            self.img = self.img_idle_left3
            self.x -= 16
            self.c_l = 1
            return 0

    def down(self):
        if self.c_d == 1:
            self.img = self.img_idle_down1
            self.y += 16
            self.c_d += 1
            return 0
        if self.c_d == 2:
            self.img = self.img_idle_down2
            self.y += 16
            self.c_d += 1
            return 0
        if self.c_d == 3:
            self.img = self.img_idle_down3
            self.y += 16
            self.c_d = 1
            return 0

    def right(self):
        if self.c_r == 1:
            self.img = self.img_idle_right1
            self.x += 16
            self.c_r += 1
            return 0
        if self.c_r == 2:
            self.img = self.img_idle_right2
            self.x += 16
            self.c_r += 1
            return 0
        if self.c_r == 3:
            self.img = self.img_idle_right3
            self.x += 16
            self.c_r = 1
            return 0

    def up(self):
        if self.c_u == 1:
            self.img = self.img_idle_up1
            self.y -= 16
            self.c_u += 1
            return 0
        if self.c_u == 2:
            self.img = self.img_idle_up2
            self.y -= 16
            self.c_u += 1
            return 0
        if self.c_u == 3:
            self.img = self.img_idle_up3
            self.y -= 16
            self.c_u = 1
            return 0

    def add_inv(self, it):
        for i in range(len(self.inv)):
            if it[0] == self.inv[i][0]:
                self.inv[i] = (self.inv[i][0], self.inv[i][1] + it[1])
                return 0
        for i in range(len(self.inv)):
            if self.inv[i] == ("0", 0):
                self.inv[i] = (it[0], it[1])
                return 0

    def del_inv(self, it):
        for i in range(len(self.inv)):
            if it[0] == self.inv[i][0]:
                self.inv[i] = (self.inv[i][0], self.inv[i][1] - it[1])
                if self.inv[i] == (self.inv[i][0], 0):
                    self.inv[i] = ("0", 0)
                    return 0
