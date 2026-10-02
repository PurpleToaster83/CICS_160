import pygame
import pygame_menu

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, color=(0,0,0), width=100, height=75, locx=0, locy=0):
        self.image            = pygame.image.load(image)
        self.width            = width
        self.height           = height
        self.x                = locx
        self.y                = locy
        

    def getImage(self):
        return(self.image)

    def getPosition(self):
        return((self.x, self.y))

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
    
    def isCollidingWith(self, theOtherVehicle):
        # print(self.getPosition())
        # print("the other object is at ", theOtherVehicle.getPosition())
        if self.getX()+self.getWidth() >= theOtherVehicle.getX() and \
            self.getX() <= theOtherVehicle.getX() + theOtherVehicle.getWidth() and \
            self.getY()  <= theOtherVehicle.getY() + theOtherVehicle.getHeight() and \
            self.getY() + self.getHeight() >= theOtherVehicle.getY():
            return (True)
        else:
            return(False)

    def getWidth(self):
        return(self.width)
    
    def getHeight(self):
        return(self.height)




