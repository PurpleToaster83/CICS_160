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
        # display go and track that race started
        if not(self.finished):
            self.started = True
            show = pygame.font.SysFont("Arial", 50).render("Go!!!", True, (255, 255, 255))
            show_rect = show.get_rect(center = (self.screen.get_width() - 500, 25))
            self.screen.blit(show, show_rect)

    def finish(self):
        # track that gmae has finished and show Game Over
        if self.started:
            self.finished = True
            show = pygame.font.SysFont("Arial", 50).render("Game Over", True, (255, 255, 255))
            show_rect = show.get_rect(center = (self.screen.get_width() - 500, 25))
            self.screen.blit(show, show_rect)

            for vehicle in self.vehicles:
                vehicle.freeze()
