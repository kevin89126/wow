from utils import get_des, image_load
import pygame

class BaseAction():

    def _check_att(self, att_tp, img):
        if att_tp == 'short':
            _des = get_des(self, img)
            if _des <= self.width + img.width:
                self.can_move = False
                return True
            return False

    def base_move(self, tg_pt):

        if not self.can_move or not tg_pt:
            return

        # check if is too close with mouse
        if abs(self.x - (tg_pt[0] - self.width/2)) < 5 and \
           abs(self.y - (tg_pt[1] - self.height/2)) < 5:
           self.can_move = False
           return

        self.img = image_load(self.imgs['std'], self.width, self.height)
        if self.x < tg_pt[0] - self.width/2:
            self.x = self.x + 1
        elif tg_pt[0] - self.width/2 < self.x:
            self.x = self.x - 1
        if  self.y < tg_pt[1] - self.height/2:
            self.y = self.y + 1
        elif tg_pt[1] - self.height/2 < self.y:
            self.y = self.y - 1

    def base_attack(self, target):
        if self.last_att == None:
            self.last_att = pygame.time.get_ticks()
        now = pygame.time.get_ticks()
        if now - self.last_att >= self.speed:
            self.img = image_load(self.imgs['att'], self.width, self.height)
            target.dmg = target.dmg + 1
            self.last_att = now
