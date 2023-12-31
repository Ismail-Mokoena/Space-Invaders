import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """Class that stores bullets for the ship"""
    def __init__(self, game_settings, screen, ship):
        """create bullet object from the ships current position"""
        super(Bullets, self). __init__()
        self.screen = screen

        # Create a bullet rect at (0,0) set at the correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                     game_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)

        self.colour = game_settings.bullet_colour
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Move the bullets up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
