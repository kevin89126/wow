import pygame
from base import BaseAction
from utils import get_des, get_click_img

class MainAction(BaseAction):

    def move(self):
        self.base_move(self.mouse)

    def check_mouse(self):
        self.click = pygame.mouse.get_pressed()[0]
        if self.click == 1:
            self.mouse = pygame.mouse.get_pos()

    def attack(self):
        img = get_click_img(self.monsters, self.mouse)
        if img == self:
            return
        if not img or not self._check_att(self.att_tp, img):
            self.last_att = None
            self.can_move = True
            return
            
        self.base_attack(img)
        if img.dmg == img.hp:
            self.reset_mouse()

    def update_monsters(self, monster=[]):
        self.monsters = monster

class MonsterAction(BaseAction):

    def move(self):
        self.base_move((self.main.x, self.main.y))

    def attack(self):
        if not self._check_att(self.att_tp, self.main):
            self.last_att = None
            self.can_move = True
            return
        self.base_attack(self.main)

    def update_main(self, main=None):
        self.main = main


