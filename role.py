from action import MainAction, MonsterAction
from utils import hp_bar_pos, draw_hp_bar, image_load

class MainRole(MainAction): 
 
    def _gen_attr(self, config): 
        for key, value in config.iteritems(): 
            self.__dict__[key] = value 
 
    def __init__(self, config): 
        self._gen_attr(config) 
        self.img = image_load(self.imgs['std'], self.width, self.height)
 
    def draw(self, surface): 
        if self.dead: 
            return 
        surface.blit(self.img, (self.x, self.y)) 
        pointlist = hp_bar_pos(self.x, self.y, 
                               self.width, self.height, 
                               self.dmg, self.hp) 
        draw_hp_bar(surface, pointlist) 
 
    def reset_mouse(self): 
        self.mouse = None 

class MonsterRole(MonsterAction): 
 
    def _gen_attr(self, config): 
        for key, value in config.iteritems(): 
            self.__dict__[key] = value 
 
    def __init__(self, config): 
        self._gen_attr(config) 
        self.img = image_load(self.imgs['std'], self.width, self.height)
 
    def draw(self, surface): 
        if self.dead: 
            return 
        surface.blit(self.img, (self.x, self.y)) 
        pointlist = hp_bar_pos(self.x, self.y, 
                               self.width, self.height, 
                               self.dmg, self.hp) 
        draw_hp_bar(surface, pointlist) 
