import pygame
import random

from pygame.locals import (RLEACCEL, K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)
pygame.init()

l = 5

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

bg = pygame.image.load("geralt-universe.jpg").convert()
bg = pygame.transform.scale(bg, (screen_width, screen_height))

class CrPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super(CrPlayer, self).__init__()
        self.surf = pygame.image.load("airplane.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)

class CrEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super(CrEnemy, self).__init__()
        self.surf = pygame.image.load("ENEMY.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrMeteor(pygame.sprite.Sprite):
    def __init__(self):
        super(CrMeteor, self).__init__()
        self.surf = pygame.image.load("meteor.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = random.randint(1, 1)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class CrShield(pygame.sprite.Sprite):
    def __init__(self):
        super(CrShield, self).__init__()
        self.surf = pygame.image.load("Shield.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()



Player = CrPlayer()
all_S = pygame.sprite.Group()
all_S.add(Player)
enemies = pygame.sprite.Group()
meteors = pygame.sprite.Group()
shields = pygame.sprite.Group()

AddEnemy = pygame.USEREVENT + 1
AddMeteor = pygame.USEREVENT + 2
AddShield = pygame.USEREVENT + 3
pygame.time.set_timer(AddEnemy, 800)
pygame.time.set_timer(AddMeteor, 5000)
pygame.time.set_timer(AddShield, 8000)

run = True
while run: #while run == true
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
        elif event.type == QUIT:
            run = False
        elif event.type == AddEnemy:
            new_enemy = CrEnemy()
            enemies.add(new_enemy)
            all_S.add(new_enemy)
        elif event.type == AddMeteor:
            new_meteor = CrMeteor()
            meteors.add(new_meteor)
            all_S.add(new_meteor)
        elif event.type == AddShield:
            new_shield = CrShield()
            shields.add(new_shield)
            all_S.add(new_shield)

    pressed_keys = pygame.key.get_pressed()
    Player.update(pressed_keys)
    enemies.update()
    meteors.update()
    shields.update()
    screen.blit(bg, (0, 0))
    for entity in all_S:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(Player, enemies):
        en = pygame.sprite.spritecollideany(Player, enemies)
        en.kill()
        l = l - 1
    if pygame.sprite.spritecollideany(Player, meteors):
        en = pygame.sprite.spritecollideany(Player, meteors)
        en.kill()
        l = l - 1
    if pygame.sprite.spritecollideany(Player, shields):
        en = pygame.sprite.spritecollideany(Player, shields)
        en.kill()
        l = l + 1

    if l == 0:
        run = False

    pygame.display.flip()