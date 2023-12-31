import pygame
from settings import *

class Transition:
    def __init__(self,reset,player):
        self.display = pygame.display.get_surface()
        self.reset = reset
        self.player = player

        # Overlay Image
        self.image = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.color = 255
        self.speed = -2

    def play(self):
        self.color += self.speed
        # Ensure we dont go below 0
        if self.color <= 0:
            self.speed *= -1
            self.color = 0
            self.reset()
        # Ensure we dont go above 255
        if self.color > 255:
            self.color = 255
            self.player.sleep = False
            self.speed = -2
            
        
        self.image.fill((self.color,self.color,self.color))
        self.display.blit(self.image, (0,0) , special_flags= pygame.BLEND_RGBA_MULT)