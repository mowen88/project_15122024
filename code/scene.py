import pygame, random
from settings import *

class Scene:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()
        self.bullet_sprite = None
        self.ship = Ship(self, self.all_sprites, (WIDTH*0.5, HEIGHT - 64*2), 300)
        self.bg = pygame.image.load('../assets/bg.png').convert_alpha()

    def create_bullet(self, pos):
        if not self.bullet_sprite:
            self.bullet_sprite = Bullet(self, self.all_sprites, pos, 900)

    def update(self, dt):
        self.all_sprites.update(dt)

    def draw(self, screen):
        screen.blit(self.bg,(0,0))
        self.all_sprites.draw(screen)
        self.game.render_text(str('FPS: '+ str(round(self.game.clock.get_fps(),2))), (255,255,255), self.game.font, (0,0), alignment='topleft')

class Ship(pygame.sprite.Sprite):
    def __init__(self, scene, groups, pos, speed):
        super().__init__(groups)
        self.scene = scene
        self.image = pygame.image.load('../assets/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = 0
        self.speed = speed

    def fire(self):
        if ACTIONS['fire']:
            self.scene.create_bullet(self.rect.center)

    def move(self):
        if ACTIONS['left']:
            self.direction = -1
        elif ACTIONS['right']:
            self.direction = 1
        else:
            self.direction = 0

    def update(self, dt):
        self.rect.x += self.direction * self.speed * dt
        self.move()
        self.fire()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, scene, groups, pos, speed):
        super().__init__(groups)
        self.scene = scene
        self.image = pygame.Surface((16,32))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self, dt):
        self.rect.y -= self.speed * dt
        if self.rect.bottom < 0:
            self.scene.bullet_sprite = None
            self.kill()

        


