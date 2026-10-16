import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class my_sprite:
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        self.sprite = pygame.image.load(image_fname) #TODO: currently not how this should be
        self.x, self.y = loc
        self.height = pygame.Surface.get_height(self.sprite)
        self.width = pygame.Surface.get_width(self.sprite)

    def get_image(self):
        return self.sprite

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

if __name__ == "__main__":
    sprite = my_sprite()