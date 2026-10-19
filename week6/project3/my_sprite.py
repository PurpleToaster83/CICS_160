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

    def get_loc(self):
        return self.loc

    def scale(self, scale_factor):
        self.original_sprite = pygame.transform.scale(self.original_sprite, (scale_factor * self.width, scale_factor * self.height))
        self.sprite = self.original_sprite
        self.height = pygame.Surface.get_height(self.sprite)
        self.width = pygame.Surface.get_width(self.sprite)

    def rotate_to(self, new_heading):
        self.heading = new_heading
        self.sprite = pygame.transform.rotate(self.original_sprite, new_heading)

    def set_location(self, loc:tuple[int, int]):
        self.loc = loc