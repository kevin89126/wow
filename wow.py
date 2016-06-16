import pygame, sys
from pygame.locals import *
from role_conf import main_config, death_config
from role import MainRole, MonsterRole

def check_death(screen, imgs):
    res = imgs[:]
    for img in res:
        if img.hp == img.dmg:
            if img.role == 'main':
                screen.fill((0,0,255))
            img.dead = True
            imgs.remove(img)
            

def check_action(action, imgs):
    for img in imgs:
        if not hasattr(img, action):
            raise Exception('Action error')
        act = getattr(img, action)
        act()

if __name__ == '__main__':
    pygame.init()
    white = (255, 255, 255)
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Hello World!')
    green = (0, 255, 0)
    red = (0, 0, 255)
    main = MainRole(main_config)
    death = MonsterRole(death_config)
    monsters = [main, death]
    main.update_monsters(monsters)
    death.update_main(main)
    clock = pygame.time.Clock()

    while True: # main game loop
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(white)
        check_death(screen, monsters)
        main.check_mouse()
        check_action('attack', monsters)
        check_action('move', monsters)
        main.draw(screen)
        death.draw(screen)
        pygame.display.update()
