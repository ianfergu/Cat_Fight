import sys
import pygame
from bullet import Bullet
pygame.init()


def check_keydown_events(event, ai_settings, screen, cats, bullets):
    if event.key == pygame.K_d:
        cats.moving_right = True
    elif event.key == pygame.K_a:
        cats.moving_left = True
    elif event.key == pygame.K_w:
        cats.moving_up = True
    elif event.key == pygame.K_s:
        cats.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, cats, bullets)
    elif event.key == pygame.K_F1:
        sys.exit()

def check_events(ai_settings, screen, cats, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, cats, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cats)


def check_keyup_events(event, cats):
    if event.key == pygame.K_d:
        cats.moving_right = False
    elif event.key == pygame.K_a:
        cats.moving_left = False
    elif event.key == pygame.K_s:
        cats.moving_down = False
    elif event.key == pygame.K_w:
        cats.moving_up = False


def update_screen(ai_settings, screen, cats, bullets, dogs):
    #screen.fill(ai_settings.bg_color)

    cats.blitme()

    for dog in dogs.sprites():
        dog.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()


def update_bullets(ai_settings, bullets, screen, dogs):
    screen_rect = screen.get_rect()
    bullets.update()

    collisions = pygame.sprite.groupcollide(bullets, dogs, True, True)

    scrn = pygame.display.get_surface()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.bottom >= screen_rect.bottom or bullet.rect.left <= 0 or bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)
        else:
            pxarray = pygame.PixelArray(screen)
            pixel = pygame.Color(pxarray[bullet.rect.centerx, bullet.rect.bottom])
            if pixel[1] == ai_settings.wall_red_val:
                bullets.remove(bullet)

    return len(dogs)


def fire_bullet(ai_settings, screen, cats, bullets):
    if ai_settings.bullets_allowed > len(bullets):
        new_bullet = Bullet(ai_settings, screen, cats)
        new_bullet.fired = False
        bullets.add(new_bullet)



