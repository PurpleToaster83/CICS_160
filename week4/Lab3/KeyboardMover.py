import pygame

class KeyboardMover():
    def __init__(self, vehicle, move_key):
        self.vehicle = vehicle
        self.move_key = move_key

    def processOneEvent(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_d]:
            self.vehicle.setPosition(self.vehicle.getX() + 1, self.vehicle.getY())
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
        return True