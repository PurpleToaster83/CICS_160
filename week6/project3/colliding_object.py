import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from my_sprite import my_sprite

class colliding_object(my_sprite):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super().__init__(image_fname, loc)

        self.bounding_box = pygame.Rect(self.loc[0], self.loc[1], self.get_width(), self.get_height())

    def get_bounding_box(self):
        return self.bounding_box

    def is_colliding_with(self, co):
        return self.bounding_box.colliderect(co.get_bounding_box())

    def rotate_to(self, new_heading):
        self.heading = new_heading
        old_center = self.bounding_box.center
        self.sprite = pygame.transform.rotate(self.original_sprite, new_heading)
        self.bounding_box = self.sprite.get_rect(center=old_center)

    def scale(self, scale_factor):
        self.bounding_box.scale_by(scale_factor)
        super().scale(scale_factor)