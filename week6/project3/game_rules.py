import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from my_sprite import my_sprite

class game_rules:
    def __init__(self, screen, vehicles):
        self.screen = screen
        self.vehicles = vehicles
        self.started = False
        self.finished = False

    def start(self):
        if not(self.finished):
            self.started = True
            show = pygame.font.SysFont("Arial", 50).render("Go!!!", True, (255, 255, 255))
            show_rect = show.get_rect(center = (self.screen.get_width() - 500, 25))
            self.screen.blit(show, show_rect)

    def finish(self):
        if self.started:
            self.finished = True
            show = pygame.font.SysFont("Arial", 50).render("Game Over", True, (255, 255, 255))
            show_rect = show.get_rect(center = (self.screen.get_width() - 500, 25))
            self.screen.blit(show, show_rect)

            for vehicle in self.vehicles:
                vehicle.freeze()

    def display_controls(self):
        controls = my_sprite("images/added/arrows.png", (self.screen.get_width() - 250, self.screen.get_height() - 200))
        controls.scale(0.1)
        self.screen.blit(controls.get_image(), controls.get_loc())

    def display_toggle(self, switch):
        # draw a rectangle in upper left corner
        display = pygame.Rect(self.screen.get_width() - 205, 0, 200, 100)
        pygame.draw.rect(self.screen, (255, 255*switch, 0), display)

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
            self.screen.blit(msg, msg_rects[m])

    def handle_collisions(self, col_obj):
        for vehicle in self.vehicles:
            for obj in col_obj:
                if vehicle.is_colliding_with(obj):
                    obj.on_collision(vehicle, self)
