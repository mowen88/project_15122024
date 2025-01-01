import pygame, sys, os
from pygame import mixer
from os import walk
from scene import Scene
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.get_joystick()
        self.accumulator = 0.0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((RES), pygame.FULLSCREEN|pygame.SCALED, vsync=0)
        self.font = pygame.font.Font(FONT, 32)
        self.scene = Scene(self)
        self.running = True

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def get_joystick(self):
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def get_events(self):
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT:
                self.quit()  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_LEFT:
                    ACTIONS['left'] = True
                if event.key == pygame.K_RIGHT:
                    ACTIONS['right'] = True
                if event.key == pygame.K_SPACE:
                    ACTIONS['fire'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ACTIONS['left'] = False
                if event.key == pygame.K_RIGHT:
                    ACTIONS['right'] = False
                if event.key == pygame.K_SPACE:
                    ACTIONS['fire'] = False

            if event.type == pygame.JOYBUTTONDOWN:
                print(event.button)
                if event.button == 13:
                    ACTIONS['left'] = True
                if event.button == 14:
                    ACTIONS['right'] = True
                if event.button == 0:
                    ACTIONS['fire'] = True

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 13:
                    ACTIONS['left'] = False
                if event.button == 14:
                    ACTIONS['right'] = False
                if event.button == 0:
                    ACTIONS['fire'] = False

    def reset_keys(self):
        for action in ACTIONS:
            ACTIONS[action] = False

    def render_text(self, text, colour, font, pos, alignment='center'):
        surf = font.render(str(text), False, colour)
        rect = surf.get_frect()  
        setattr(rect, alignment, pos) 
        self.screen.blit(surf, rect)

    def update(self, dt):
        self.scene.update(dt)
 
    def draw(self, screen):
        self.scene.draw(screen)
        pygame.display.update()

    def loop(self):
        dt = self.clock.tick() * 0.001

        self.accumulator += dt
        while self.accumulator >= FIXED_DT:
            self.accumulator -= FIXED_DT
            self.update(FIXED_DT)
            self.get_events()

        self.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    while game.running:
        game.loop()
       