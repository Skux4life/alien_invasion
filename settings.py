import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's settings'"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point value increases
        self.score_scale = 1.5
        
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_speed = 1.0
        # fleet_direction of 1 means right and -1 means left
        self.fleet_direction = 1
        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        