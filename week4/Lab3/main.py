import pygame
import Vehicle

def main():
    pygame.init()
    canvas      = pygame.display.set_mode((1240, 820))
    car1        = Vehicle.Vehicle("./Images/orange_truck.png")
    tree        = Vehicle.Vehicle("./Images/tree.png", locx=1000)
    keepRunning = True
    while (keepRunning):
        canvas.blit(car1.getImage(),car1.getPosition())
        canvas.blit(tree.getImage(),tree.getPosition())
        pygame.display.flip()
        if car1.isCollidingWith(tree):
            print("the car and the tree have collided!!!")
        pressedKeys =  pygame.key.get_pressed()
        if pressedKeys[pygame.K_d]:
            car1.setPosition(car1.getX() + 1, car1.getY())
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keepRunning = False


if __name__ == "__main__":
    main()