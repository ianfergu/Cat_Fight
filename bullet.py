import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, cats):
        super().__init__()
        self.screen = screen
        self.cats = cats

        self.image = pygame.image.load("/Users/Ian/Desktop/yarn.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = cats.rect.centerx
        self.rect.top = cats.rect.top

        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

        self.fired = False

    def update(self):
        if self. cats.pointer == 1 and not self.fired:
            self.y -= self.speed_factor
        elif self.cats.pointer == 2 and not self.fired:
            self.rect.centerx += self.speed_factor
        elif self.cats.pointer == 3 and not self.fired:
            self.y += self.speed_factor
        elif self.cats.pointer == 4 and not self.fired:
            self.rect.centerx -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
