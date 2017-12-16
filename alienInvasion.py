import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import bullet

def run_game():

    ##初始化并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screenheight))
    pygame.display.set_caption("Alien invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()

    bg_color=(230,230,230)

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        #bullets.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings,screen,ship,bullets)

        # for bullet in bullets.copy():
        #     if bullet.rect.bottom<=0:
        #         bullets.remove(bullet)
        #print(len(bullets))

run_game()