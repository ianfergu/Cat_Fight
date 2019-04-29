import pygame

class Settings():
    def __init__(self, bullet_spd, cat_spd):
        screen = pygame.image.load("/Users/Ian/Desktop/map1.png")
        screen = screen.get_rect()

        self.screen_width = screen.width
        self.screen_height = screen.height
        self.bg_color = (200, 200, 200)

        self.cat_speed_factor = cat_spd

        self.bullet_speed_factor = bullet_spd
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1

        self.wall_red_val = 0