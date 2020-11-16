class Settings:
    """A class that stores all of the the settings from alien invasion"""

    def __init__(self):
        """initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 170, 250)
        # Ship Settings
        self.ship_speed = 0.75
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)