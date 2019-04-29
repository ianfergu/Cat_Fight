import pygame


class Cat():
    def __init__(self, ai_settings, screen, cat_x, cat_y):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("/Users/Ian/Desktop/cat.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = cat_x
        self.rect.bottom = cat_y

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.pointer = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.cat_speed_factor
            self.pointer = 2
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.cat_speed_factor
            self.pointer = 4
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.cat_speed_factor
            self.pointer = 3
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.cat_speed_factor
            self.pointer = 1

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
