import pygame
import Vehicle

import pygame
import Vehicle
import KeyboardMover

def main():
    canvas = pygame.display.set_mode((1240, 820))
    car1 = Vehicle.Vehicle("./Images/orange_truck.png")
    redcar = Vehicle.Vehicle("./Images/red_car.png")
    kbReader = KeyboardMover.KeyboardMover(car1, "l")
    reader2 = KeyboardMover.KeyboardMover(redcar, 'd')
    keepRunning = True
    while (keepRunning):
        canvas.blit(car1.getImage(),car1.getPosition())
        canvas.blit(redcar.getImage(),redcar.getPosition())
        pygame.display.flip()
        keepRunning = kbReader.processOneEvent() and reader2.processOneEvent()
                    
if __name__ == "__main__":
    main()