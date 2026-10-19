import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from colliding_object import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super().__init__(image_fname, loc)
        self.can_move = True
        self.crashed = False

    # def set_location(self, loc:tuple[int, int]):
    #     self.loc = loc
    #     self.bounding_box.left = loc[0]
    #     self.bounding_box.top = loc[1]

    def move_vehicle(self, step):
        if self.can_move:
            pressedKeys = pygame.key.get_pressed()
            cur_x, cur_y = self.loc
            new_heading = self.heading

            if pressedKeys[pygame.K_UP]:
                cur_y -= step
                new_heading = 90
            elif pressedKeys[pygame.K_DOWN]:
                cur_y += step
                new_heading = 270
            elif pressedKeys[pygame.K_LEFT]:
                cur_x -= step
                new_heading = 180
            elif pressedKeys[pygame.K_RIGHT]:
                cur_x += step
                new_heading = 0

            self.set_location((cur_x, cur_y))

            if new_heading != self.heading:
                self.rotate_to(new_heading)

    def switch_can_move(self):
        self.can_move = False

    def crash(self, image_path):
        self.crashed = True
        self.can_move = False
        super().change_image(image_path)