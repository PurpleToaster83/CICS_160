import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, color=(0,0,0), width=186, height=76, locx=0, locy=0):
        self.image            = pygame.image.load(image)
        self.width            = width
        self.height           = height
        self.x                = locx
        self.y                = locy
        

    def getImage(self):
        return(self.image)

    def IsCollidingWith(self, otherObject):
        other_position = otherObject.getX()
        if self.x + 186 >= other_position and self.x <= other_position + 186:
            return True

    def getPosition(self):
        return((self.x, self.y))

    def getWidth(self):
        return(self.width)

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)



