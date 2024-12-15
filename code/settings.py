import pygame

FPS = 60
FIXED_DT = 1/60
RES = WIDTH, HEIGHT = pygame.math.Vector2(960, 540)
HALF_WIDTH, HALF_HEIGHT = RES/2
ASPECT_RATIO = (WIDTH/HEIGHT)
FONT = '../assets/homespun.ttf'
ACTIONS = {'left':False,'right':False,'fire':False}