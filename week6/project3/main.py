import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from moving_vehicle import moving_vehicle
from colliding_object import colliding_object
from my_sprite import my_sprite

def display_control(surface, switch):

    # draw a rectangle in upper left corner
    display = pygame.Rect(surface.get_width() - 205, 0, 200, 100)
    pygame.draw.rect(surface, (255, 255*switch, 0), display)

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
        surface.blit(msg, msg_rects[m])

def prep_images(screen, image_list, scale_factor):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # image_list: [0:11] road sprites, [12:16] colliding objects, [17:18] vehicles
    image_list[12].scale(scale_factor / 2)
    image_list[12].rotate_to(90)
    image_list[13].scale(scale_factor / 2)
    image_list[13].rotate_to(90)
    image_list[15].scale((2/3) * scale_factor)
    image_list[16].scale(2 * scale_factor)

    for img in image_list[:12]:
        img.scale(scale_factor)
    image_list[1].scale(4.5 * scale_factor)
    image_list[9].scale(4.5 * scale_factor)
    image_list[4].rotate_to(90)
    image_list[5].rotate_to(90)
    image_list[6].rotate_to(270)
    image_list[11].rotate_to(90)

    road_start = screen_height - image_list[0].get_height() - 10
    correction = 50 * scale_factor

    locs = [
        (screen_width / 8, road_start),
        ((screen_width / 8) + image_list[0].get_width(), road_start),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width(), road_start),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width() + image_list[2].get_width(), road_start),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width() + image_list[2].get_width() + image_list[3].get_width() - correction, road_start - image_list[4].get_width() + correction),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width() + image_list[2].get_width() + image_list[3].get_width() - correction, road_start),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width() + image_list[2].get_width() + image_list[3].get_width() - correction, road_start - image_list[5].get_width() - image_list[4].get_width() + 2*correction),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width() + image_list[2].get_width(), road_start - image_list[5].get_width() - image_list[4].get_width() + 2*correction),
        ((screen_width / 8) + image_list[0].get_width() + image_list[1].get_width(), road_start - image_list[5].get_width() - image_list[4].get_width() + 2*correction),
        ((screen_width / 8) + image_list[0].get_width(), road_start - image_list[5].get_width() - image_list[4].get_width() + 2*correction),
        ((screen_width / 8) - (image_list[10].get_width() / 3), road_start - image_list[5].get_width() - image_list[4].get_width() - (image_list[10].get_height() / 6)),
        ((screen_width / 8) + image_list[0].get_width(), road_start - (image_list[11].get_width())),

        ((screen_width / 8) - (image_list[12].get_height() / 2) + 5 * correction, road_start),
        ((screen_width / 8) - (image_list[12].get_height() / 2) - 6 * correction, road_start - image_list[5].get_width() - image_list[4].get_width() - (image_list[10].get_height() / 6)),
        ((screen_width / 8) + image_list[0].get_width(), road_start - image_list[5].get_width() - image_list[4].get_width() - (image_list[10].get_height() / 2)),
        ((screen_width / 6) + image_list[0].get_width(), (screen_height / 2) - correction),
        ((screen_width / 2) - 2 * correction, (screen_height / 2) + correction),

        (0, road_start + correction),
        (0, road_start + 0.5 * image_list[0].get_height() + correction)
    ]

    for i, img in enumerate(image_list):
        img.set_location(locs[i])

def handle_collisions(screen, images):
    start = False
    finish = False

    for idx in (17, 18):
        vehicle = images[idx]
        if vehicle.is_colliding_with(images[14]) or vehicle.is_colliding_with(images[16]):
            vehicle.crash("images/added/explosion.png")
        if vehicle.is_colliding_with(images[15]):
            images[15].change_image("images/added/blood.png")
        if vehicle.is_colliding_with(images[12]):
            start = True
        if vehicle.is_colliding_with(images[13]):
            start = False
            finish = True

    if start:
        msg = pygame.font.SysFont("Arial", 50).render(f'Go!!!', True, (255, 255, 255))
        msg_rect = msg.get_rect(center = (screen.get_width() - 500, 25))
        screen.blit(msg, msg_rect)
    elif finish:
        msg = pygame.font.SysFont("Arial", 50).render(f'Game Over', True, (255, 255, 255))
        msg_rect = msg.get_rect(center = (screen.get_width() - 500, 25))
        screen.blit(msg, msg_rect)
        images[17].switch_can_move()
        images[18].switch_can_move()

def main():
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True

    control_yellow = True
    scale_factor = 0.3
    images = [
        my_sprite("images/road/road_straight.png", (0,0)),
        my_sprite("images/road/road_intersection.png", (0,0)),
        my_sprite("images/road/road_straight_alt.png", (0,0)),
        my_sprite("images/road/road_straight.png", (0,0)),
        my_sprite("images/road/road_straight.png", (0,0)),
        my_sprite("images/road/road_turn_down.png", (0,0)),
        my_sprite("images/road/road_turn_up.png", (0,0)),
        my_sprite("images/road/road_straight_alt.png", (0,0)),
        my_sprite("images/road/road_straight.png", (0,0)),
        my_sprite("images/road/road_intersection.png", (0,0)),
        my_sprite("images/road/road_bend_down.png", (0,0)),
        my_sprite("images/road/road_straight.png", (0,0)),

        colliding_object("images/decor/Start.png", (0,0)),
        colliding_object("images/decor/Finish.png", (0,0)),
        colliding_object("images/decor/tree.png", (0,0)),
        colliding_object("images/added/walking_person.png", (0,0)),
        colliding_object("images/decor/tree.png", (0,0)),

        moving_vehicle("images/vehicles/red_car.png", (0,0)),
        moving_vehicle("images/vehicles/yellow_convertible.png", (0,0))
    ]

    prep_images(screen, images, scale_factor)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                control_yellow = not(control_yellow)

        if control_yellow:
            images[18].move_vehicle(8)
        else:
            images[17].move_vehicle(5)

        screen.fill((0, 0, 0))

        for img in images:
            screen.blit(img.get_image(), img.get_loc())

        # show control relevant info
        display_control(screen, control_yellow)
        handle_collisions(screen, images)

        #TODO: make sure follows SOLID Princples

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()