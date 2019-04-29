import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, ai_settings, screen, cats, bullets, x_start, y_start):
        super().__init__()
        self.screen = screen
        self.cats = cats
        self.ai_settings = ai_settings

        self.image = pygame.image.load("/Users/Ian/Desktop/doggy.png")
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect

        self.rect.centerx = x_start
        self.rect.bottom = y_start

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def die(self):
        self.image.fill(self.ai_settings.bg_color)






