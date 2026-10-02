import pygame
import Vehicle

import pygame
import Vehicle
import KeyboardMover

def main():
    canvas = pygame.display.set_mode((1240, 820))
    car1 = Vehicle.Vehicle("./Images/orange_truck.png")
    kbReader = KeyboardMover.KeyboardMover(car1, "d")
    keepRunning = True
    while (keepRunning):
        canvas.blit(car1.getImage(),car1.getPosition())
        pygame.display.flip()
        keepRunning = kbReader.processOneEvent()
                    
if __name__ == "__main__":
    main()