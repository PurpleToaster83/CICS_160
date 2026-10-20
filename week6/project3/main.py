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
        rules.display_toggle(control_yellow)
        rules.display_controls()
        rules.handle_collisions(col_obj)
        for img in (road_pieces + col_obj + vehicles):
            screen.blit(img.get_image(), img.get_loc())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()