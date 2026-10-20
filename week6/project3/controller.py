import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class controller:
    def arrow_pressed(self):
        arrows = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_UP]:
            arrows["up"] = True
        if pressedKeys[pygame.K_DOWN]:
            arrows["down"] = True
        if pressedKeys[pygame.K_LEFT]:
            arrows["left"] = True
        if pressedKeys[pygame.K_RIGHT]:
            arrows["right"] = True

        return arrows
            