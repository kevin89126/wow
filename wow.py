import pygame, sys
from pygame.locals import *
from role_conf import main_config, death_config
from role import MainRole, MonsterRole

def check_death(screen, imgs, death_mons):
    res = imgs[:]
    for img in res:
        if img.hp == img.dmg and not img.dead:
            if img.role == 'main':
                screen.fill((0,0,255))
            img.dead = pygame.time.get_ticks()
            imgs.remove(img)
            death_mons.append(img)

def check_bron(screen, imgs, death_mons):
    res = death_mons[:]
    for img in res:
        now = pygame.time.get_ticks()
        print img.dead, now
        if img.dead and now - img.dead > img.reborn_time:
            img.dead = 0
            img.dmg = 0
            imgs.append(img)
            death_mons.remove(img)

def check_action(action, imgs):
    for img in imgs:
        if img.dead:
            return
        if not hasattr(img, action):
            raise Exception('Action error')
        act = getattr(img, action)
        act()

if __name__ == '__main__':
    pygame.init()
    white = (255, 255, 255)
    screen = pygame.display.set_mode((1024, 2048))
    pygame.display.set_caption('Hello World!')
    green = (0, 255, 0)
    red = (0, 0, 255)
    main = MainRole(main_config)
    death = MonsterRole(death_config)
    monsters = [death]
    dead_mons = []
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
        main.update_monsters(monsters)
        death.update_main(main)
        print monsters
        check_bron(screen, monsters, dead_mons)
        check_death(screen, monsters, dead_mons)
        main.check_mouse()
        check_action('attack', [main])
        check_action('attack', monsters)
        check_action('move', [main])
        check_action('move', monsters)
        main.draw(screen)
        death.draw(screen)
        pygame.display.update()
