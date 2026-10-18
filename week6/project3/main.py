import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from moving_vehicle import moving_vehicle
from colliding_object import colliding_object
from my_sprite import my_sprite

def main():
    
    locs = [
        (0, 0),
        (10, 10),
        (20, 20),
        (30, 30),
        (40, 40),
        (50, 50),
        (60, 60),
        (70, 70),
        (80, 80),
        (90, 90),
        (100, 100),
        (110, 110)
    ]

    # 2 moving_vehicles
    veh1 = moving_vehicle("images/vehicles/red_car.png", locs[0])
    veh2 = moving_vehicle("images/vehicles/yellow_convertible.png", locs[1])

    # 5 colliding objects
    col_obj1 = colliding_object("images/decor/Finish.png", locs[2])
    col_obj2 = colliding_object("images/decor/Start.png", locs[3])
    col_obj3 = colliding_object("images/decor/tree.png", locs[4])
    col_obj4 = colliding_object("images/decor/Finish.png", locs[5])
    col_obj5 = colliding_object("images/decor/Start.png", locs[6])

    # 5 decoaration sprites
    sprite1 = my_sprite("images/road/road_bend_down.png", locs[7])
    sprite2 = my_sprite("images/road/road_intersection.png", locs[8])
    sprite3 = my_sprite("images/road/road_straight_alt.png", locs[9])
    sprite4 = my_sprite("images/road/road_turn_down.png", locs[10])
    sprite5 = my_sprite("images/road/road_straight.png", locs[11])


    #TODO: write the functionality to controll in helper functions
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(sprite1.get_image(), sprite1.loc)
        pygame.display.flip()
        clock.tick()
    pygame.quit()

if __name__ == "__main__":
    main()