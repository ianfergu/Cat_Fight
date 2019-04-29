import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from cat import Cat
import game_functions as gf
from Enemy import Enemy


def run_game(source_file="/Users/Ian/Desktop/map1.png", x_start=600, y_start=80, bullet_spd=2,
             cat_spd=1, cat_x=1, cat_y=0):

    pygame.init()
    ai_settings = Settings(bullet_spd, cat_spd)

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    bg = pygame.image.load(source_file).convert()

    pygame.display.set_caption("Cat Fight")

    cats = Cat(ai_settings, screen, cat_x, cat_y)
    bullets = Group()
    dogs = Group()
    dog = Enemy(ai_settings, screen, cats, bullets, x_start, y_start)
    dogs.add(dog)
    enemies = 1

    while enemies == 1:
        gf.check_events(ai_settings, screen, cats, bullets)
        screen.blit(bg, (0, 0))
        cats.update()
        enemies = gf.update_bullets(ai_settings, bullets, screen, dogs)
        gf.update_screen(ai_settings, screen, cats, bullets, dogs)
