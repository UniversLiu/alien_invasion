import sys
import pygame
from settings import setting
from ship import Ship
import game_function as gf
#导入模块


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = setting()    
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_heigh))
    pygame.display.set_caption('Alien Invasion')
        
    #创建一艘飞船
    ship = Ship(ai_settings,screen)


    #开始游戏主循环
    while True:

        #监视鼠标和键盘
        gf.check_events(ship)

        #更新飞机位置
        ship.update()

        #重绘屏幕颜色   
        gf.update_screen(ai_settings,screen,ship)

        #最近绘制屏幕可见
        pygame.display.flip()
    
run_game()
