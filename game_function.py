import sys
import pygame
import settings
from ship import Ship
#导入模块

def check_events(ship):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right =True                    
            elif event.key == pygame.K_LEFT:
                ship.moving_left =True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False 
            elif event.key == pygame.K_LEFT:
                ship.moving_left= False 

def update_screen(ai_settings,screen,ship):
    '''更新屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()