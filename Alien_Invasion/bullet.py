import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def _init_(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super()._init_()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.setting.bullet_color

        # Create a bullet rect at (0, 0) then move it to the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings,bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position aa a decimal point
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)