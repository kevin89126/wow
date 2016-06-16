import pygame, sys
from pygame.locals import *
from math import sqrt
from constants import green

def image_load(path, width, height):
    pic = pygame.image.load(path)
    pic = pygame.transform.scale(pic, (width, height))
    return pic

def get_click_img(img_info, mouse):
    if not mouse:
        return {}
    for pic in img_info:
        if pic.x < mouse[0] < pic.x + pic.width and \
           pic.y < mouse[1] < pic.y + pic.height:
            return pic
    return {}

def get_img(name):
    for img in imgs:
        if img.name == name:
            return img

def get_des(a, b):
    return int(sqrt((a.x - b.x)**2 + (a.y - b.y)**2))

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
