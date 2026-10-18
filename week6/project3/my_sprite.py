import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class my_sprite:
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        self.image_fname = image_fname
        self.loc = loc

        # create an original sprite and then another that will be returned
        self.original_sprite = pygame.image.load(self.image_fname)
        self.sprite = self.original_sprite

        # keep track of sprite attributes
        self.original_height = pygame.Surface.get_height(self.original_sprite)
        self.original_width = pygame.Surface.get_width(self.original_sprite)
        self.height = pygame.Surface.get_height(self.sprite)
        self.width = pygame.Surface.get_width(self.sprite)
        self.heading = 0

    def get_image(self):
        return self.sprite

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def scale(self, scale_factor):
        ratio  = (self.height / self.original_height) * scale_factor
        self.original_sprite = pygame.transform.scale(self.original_sprite, (ratio * self.width, ratio * self.height))
        self.height = pygame.Surface.get_height(self.sprite)
        self.width = pygame.Surface.get_width(self.sprite)