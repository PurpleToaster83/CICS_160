import pygame
import Vehicle

def main():
    pygame.init()
    canvas = pygame.display.set_mode((1240, 820))
    car1 = Vehicle.Vehicle("./Images/green_car.png")
    keepRunning = True
    while (keepRunning):
        canvas.blit(car1.getImage(),car1.getPosition())
        pygame.display.flip()
        pressedKeys =  pygame.key.get_pressed()
        if pressedKeys[pygame.K_d]:
            car1.setPosition(car1.getX() + 1, car1.getY())
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keepRunning = False


if __name__ == "__main__":
    main()