import pygame, sys
from pygame.locals import *
from img import ImgManager
import time

def image_load(path, width, height):
    pic = pygame.image.load(path)
    pic = pygame.transform.scale(pic, (width, height))
    return pic

def get_click_img(img_info, mouse):
    for pic in img_info:
        if pic.x < mouse[0] < pic.x + pic.width and \
           pic.y < mouse[1] < pic.y + pic.height:
            return pic
    return {}

def get_img(name):
    for img in imgs:
        if img.name == name:
            return img

class Action():

    def move(self):   #function in which i am moving image
        self.click = pygame.mouse.get_pressed()[0]

        if self.click == 1:
            self.drag = 1
            self.mouse = pygame.mouse.get_pos()
            self.img = image_load(self.std, self.width, self.height)

        if abs(self.x - (self.mouse[0] - self.width/2)) < 5 and \
           abs(self.y - (self.mouse[1] - self.height/2)) < 5:
           return

        img = get_click_img(imgs, self.mouse)
        if img:
            return

        if self.drag == 1:   #moving the image
            if self.x < self.mouse[0] - self.width/2:
                self.x = self.x + 1
            elif self.mouse[0] - self.width/2 < self.x:
                self.x = self.x - 1
            if  self.y < self.mouse[1] - self.height/2:
                self.y = self.y + 1
            elif self.mouse[1] - self.height/2 < self.y:
                self.y = self.y - 1

    def attack(self):
        img = get_click_img(imgs, self.mouse)
        if not img:
            self.last_att = None
            return
        self.drag = 0
        if self.last_att == None:
            self.last_att = pygame.time.get_ticks()
        now = pygame.time.get_ticks()
        print now, self.last_att
        if now - self.last_att >= self.speed:
            self.img = image_load(self.att, self.width, self.height)
            img.dmg = img.dmg + 1
            self.last_att = now

def hp_bar_pos(x, y, width, height, dmg, hp):
    return [
        (x,
         y+height
        ),
        (x+width-(width/hp)*dmg,
         y+height
        )
    ]
 

def draw_hp_bar(screen, pointlist):
    pygame.draw.lines(screen, green, False, pointlist, 5)


class Role(Action):

    def __init__(self, name, imgs, width, height, x, y):
        self.att = imgs.get('att', '')
        self.std = imgs.get('std', '')
        self.name = name
        self.width = width
        self.height = height
        self.img = image_load(self.std, width, height)
        self.click = 0
        self.drag = 0
        self.lock_mouse = 0
        self.x = x
        self.y = y
        self.hp = 10
        self.mouse = (self.x ,self.y)
        self.dead = False
        self.dmg = 0
        self.speed = 1000
        self.last_att = None

    def draw(self, surface):
        if self.dead:
            return
        surface.blit(self.img, (self.x, self.y))
        pointlist = hp_bar_pos(self.x, self.y,
                               self.width, self.height,
                               self.dmg, self.hp)
        draw_hp_bar(surface, pointlist)
        

def check_death():
    res = imgs[:]
    for img in res:
        if img.hp == img.dmg:
            img.dead = True
            imgs.remove(img)

if __name__ == '__main__':
    pygame.init()
    img_mgr = ImgManager()
    white = (255, 255, 255)
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Hello World!')
    imgWidth = 50
    imgHeight = 100
    green = (0, 255, 0)
    which_imgs = img_mgr.which
    print which_imgs
    death_imgs = img_mgr.death
    whitch = Role('which', which_imgs, imgWidth, imgHeight, 100, 100)
    death = Role('death', death_imgs, imgHeight, imgHeight, 300, 250)
    global imgs 
    imgs = [death]
    clock = pygame.time.Clock()

    while True: # main game loop
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(white)
        check_death()
        whitch.move()
        whitch.attack()
        whitch.draw(screen)
        death.draw(screen)
        pygame.display.update()
