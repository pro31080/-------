import pygame

SURFACE_WIDTH=300
SURFACE_HEIGHT=250
SURFACE_COLOR=(0, 255, 255)
SURFACE_FPS=60

def prepare()->pygame.Surface:
    pygame.init()
    ret=pygame.display.set_mode(SURFACE_WIDTH,SURFACE_HEIGHT)
    pygame.display.update()
    return ret    

surface = prepare()


pygame.quit()

