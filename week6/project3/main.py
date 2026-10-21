import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from game_rules import game_rules
from moving_vehicle import moving_vehicle
from start import start
from finish import finish
from tree import tree
from pedestrian import pedestrian
from my_sprite import my_sprite
from controller import controller

def prep_images(screen, sprites, col_obj, vehicles, scale_factor):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # scale and rotate images
    col_obj[0].scale(scale_factor / 2)
    col_obj[0].rotate_to(90)
    col_obj[1].scale(scale_factor / 2)
    col_obj[1].rotate_to(90)
    col_obj[3].scale((2/3) * scale_factor)
    col_obj[4].scale(2 * scale_factor)

    for img in sprites:
        img.scale(scale_factor)
    sprites[1].scale(4.5 * scale_factor)
    sprites[9].scale(4.5 * scale_factor)
    sprites[4].rotate_to(90)
    sprites[5].rotate_to(90)
    sprites[6].rotate_to(270)
    sprites[11].rotate_to(90)

    road_start = screen_height - sprites[0].get_height() - 10
    correction = 50 * scale_factor

    # calculate locations based on image specific info
    # requires images to be initialized before-hand and then moved
    locs = [
        (screen_width / 8, road_start),
        ((screen_width / 8) + sprites[0].get_width(), road_start),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width(), road_start),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width() + sprites[2].get_width(), road_start),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width() + sprites[2].get_width() + sprites[3].get_width() - correction, road_start - sprites[4].get_width() + correction),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width() + sprites[2].get_width() + sprites[3].get_width() - correction, road_start),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width() + sprites[2].get_width() + sprites[3].get_width() - correction, road_start - sprites[5].get_width() - sprites[4].get_width() + 2*correction),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width() + sprites[2].get_width(), road_start - sprites[5].get_width() - sprites[4].get_width() + 2*correction),
        ((screen_width / 8) + sprites[0].get_width() + sprites[1].get_width(), road_start - sprites[5].get_width() - sprites[4].get_width() + 2*correction),
        ((screen_width / 8) + sprites[0].get_width(), road_start - sprites[5].get_width() - sprites[4].get_width() + 2*correction),
        ((screen_width / 8) - (sprites[10].get_width() / 3), road_start - sprites[5].get_width() - sprites[4].get_width() - (sprites[10].get_height() / 6)),
        ((screen_width / 8) + sprites[0].get_width(), road_start - (sprites[11].get_width())),

        ((screen_width / 8) - (col_obj[0].get_height() / 2) + 5 * correction, road_start),
        ((screen_width / 8) - (col_obj[0].get_height() / 2) - 6 * correction, road_start - sprites[5].get_width() - sprites[4].get_width() - (sprites[10].get_height() / 6)),
        ((screen_width / 8) + sprites[0].get_width(), road_start - sprites[5].get_width() - sprites[4].get_width() - (sprites[10].get_height() / 2)),
        ((screen_width / 6) + sprites[0].get_width(), (screen_height / 2) - correction),
        ((screen_width / 2) - 2 * correction, (screen_height / 2) + correction),

        (0, road_start + correction),
        (0, road_start + 0.5 * sprites[0].get_height() + correction)
    ]

    # set all the proper locations
    for i, img in enumerate(sprites + col_obj + vehicles):
        img.set_location(locs[i])

def display_controls(screen):
    # show arrow png on screen in corner
    controls = my_sprite("images/added/arrows.png", (screen.get_width() - 250, screen.get_height() - 200))
    controls.scale(0.1)
    screen.blit(controls.get_image(), controls.get_loc())

def display_toggle(screen, switch):
    # draw a rectangle in upper left corner
    display = pygame.Rect(screen.get_width() - 205, 0, 200, 100)
    pygame.draw.rect(screen, (255, 255*switch, 0), display)

    # messages to be displayed in rectangle
    msgs = [
        pygame.font.SysFont("Arial", 20).render(f'Controlling:', True, (0, 0, 0)),
        pygame.font.SysFont("Arial", 25).render(" Yellow" if switch else " Red", True, (0, 0, 0)),
        pygame.font.SysFont("Arial", 15).render(f'Click SPACE to Switch', True, (0, 0, 0))
    ]

    # bounding boxes for the messages
    msg_rects = [
        msgs[0].get_rect(center = (display.centerx, display.centery - 30)),
        msgs[1].get_rect(center = display.center),
        msgs[2].get_rect(center = (display.centerx, display.centery + 40))
    ]

    # draw each message and its bounding box
    for m, msg in enumerate(msgs):
        screen.blit(msg, msg_rects[m])

def handle_collisions(col_obj, vehicles, rules):
    # check if any vehicle is collding with an object
    for vehicle in vehicles:
        for obj in col_obj:
            # if vehicle is collding notify the object
            if vehicle.is_colliding_with(obj):
                obj.on_collision(vehicle, rules)

def main():
    # initialize pygame stuff
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True

    control_yellow = True
    scale_factor = 0.3

    # create sprites, colliding_objects, and vehicles at (0,0)
    road_pieces = [
        my_sprite("images/road/road_straight.png"),
        my_sprite("images/road/road_intersection.png"),
        my_sprite("images/road/road_straight_alt.png"),
        my_sprite("images/road/road_straight.png"),
        my_sprite("images/road/road_straight.png"),
        my_sprite("images/road/road_turn_down.png"),
        my_sprite("images/road/road_turn_up.png"),
        my_sprite("images/road/road_straight_alt.png"),
        my_sprite("images/road/road_straight.png"),
        my_sprite("images/road/road_intersection.png"),
        my_sprite("images/road/road_bend_down.png"),
        my_sprite("images/road/road_straight.png")
    ]

    col_obj = [
        start("images/decor/Start.png"),
        finish("images/decor/Finish.png"),
        tree("images/decor/tree.png"),
        pedestrian("images/added/walking_person.png"),
        tree("images/decor/tree.png")
    ]

    controllers = [
        controller(),
        controller()
    ]

    vehicles = [
        moving_vehicle("images/vehicles/red_car.png", controller=controllers[0]),
        moving_vehicle("images/vehicles/yellow_convertible.png", controller=controllers[1])
    ]

    # create rules and move images to correct locations
    rules = game_rules(screen, vehicles)
    prep_images(screen, road_pieces, col_obj, vehicles, scale_factor)

    while running:
        # check if quite or spacebar car toggle is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                control_yellow = not(control_yellow)

        # control car based on toggle
        vehicles[control_yellow].move_vehicle(5 + (3 * control_yellow))

        # reset screen
        screen.fill((0, 0, 0))

        # draw all the images 
        display_toggle(screen, control_yellow)
        display_controls(screen)
        handle_collisions(col_obj, vehicles, rules)
        for img in (road_pieces + col_obj + vehicles):
            screen.blit(img.get_image(), img.get_loc())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()