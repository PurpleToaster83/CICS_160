import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from moving_vehicle import moving_vehicle
from colliding_object import colliding_object
from my_sprite import my_sprite

def move_vehicle(vehicle, step):
    pressedKeys = pygame.key.get_pressed()
    cur_x, cur_y = vehicle.loc
    new_heading = vehicle.heading

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

    vehicle.set_location((cur_x, cur_y))

    if new_heading != vehicle.heading:
        vehicle.rotate_to(new_heading)

def main():

    locs = [
        (0, 0),
        (20, 20),
        (40, 40),
        (60, 60),
        (80, 80),
        (100, 100),
        (120, 120),
        (140, 140),
        (160, 160),
        (180, 180),
        (200, 200),
        (220, 220)
    ]

    # 2 moving_vehicles
    vehicles = [
        moving_vehicle("images/vehicles/red_car.png", locs[0]),
        moving_vehicle("images/vehicles/yellow_convertible.png", locs[1])
    ]


    # 5 colliding objects
    col_obj = [
        colliding_object("images/decor/Finish.png", locs[2]),
        colliding_object("images/decor/Start.png", locs[3]),
        colliding_object("images/decor/tree.png", locs[4]),
        colliding_object("images/decor/Finish.png", locs[5]),
        colliding_object("images/decor/Start.png", locs[6])
    ]


    # 5 decoaration sprites
    sprites = [
        my_sprite("images/road/road_bend_down.png", locs[7]),
        my_sprite("images/road/road_intersection.png", locs[8]),
        my_sprite("images/road/road_straight_alt.png", locs[9]),
        my_sprite("images/road/road_turn_down.png", locs[10]),
        my_sprite("images/road/road_straight.png", locs[11]),
    ]


    images = vehicles + col_obj + sprites

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    control_yellow = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                control_yellow = not(control_yellow)

        if control_yellow:
            move_vehicle(vehicles[1], 8)
        else:
            move_vehicle(vehicles[0], 5)
        screen.fill((0, 0, 0))

        screen.blit(vehicles[0].get_image(), vehicles[0].loc)
        screen.blit(vehicles[1].get_image(), vehicles[1].loc)

        #TODO: put this all into a function
        #TODO: put other sprites in
        #TODO: collision detection in move_vehicle
        #TODO: make it more dynamic
        #TODO: make sure follows SOLID Princples
        
        display = pygame.Rect(0, 0, 100, 100)
        pygame.draw.rect(screen, (255, 255*control_yellow, 0), display)
        msg = pygame.font.SysFont("Arial", 15).render(f'Controlling', True, (0, 0, 0))
        color = pygame.font.SysFont("Arial", 20).render(" Yellow" if control_yellow else " Red", True, (0, 0, 0))
        switch = pygame.font.SysFont("Arial", 8).render(f'Click SPACE to Switch', True, (0, 0, 0))
        msg_rect = msg.get_rect(center = (display.centerx, display.centery - 30))
        color_rect = color.get_rect(center = display.center)
        switch_rect = switch.get_rect(center = (display.centerx, display.centery + 40))
        screen.blit(msg, msg_rect)
        screen.blit(color, color_rect)
        screen.blit(switch, switch_rect)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()