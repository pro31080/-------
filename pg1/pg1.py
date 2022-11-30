import pygame

WIDTH=300
HEIGHT=300

pygame.init()


def prepare()->pygame.Surface:
    pygame.init()
    ret=pygame.display.set_mode(WIDTH,HEIGHT)
    pygame.display.update()
    return ret    

surface = prepare()