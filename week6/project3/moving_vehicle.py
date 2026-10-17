import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super.__init__(image_fname, loc)

    def set_location(self, loc:tuple[int, int]):
        self.x = loc[0]
        self.y = loc[1]
        pygame.display.update()