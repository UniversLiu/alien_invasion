class setting():
    '''存储游戏所需设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''

        #屏幕设置
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_speed_factor = 1.5