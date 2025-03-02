# pacman class is gonna be here
import pygame
from basecharacter import Guy
from blinkychar import Blinky


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

guy = Guy((31, 15), 30, (0, 0))
guy.render_loc(screen)
ghost1 = Blinky((31, 15), 30, (0, 0))
ghost1.render_loc_ghost(screen)
ghost1.set_speed(2)

dirr = None
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    guy.temp_board_render(screen)
    action = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_UP:
                guy.move(3, screen)
                action = 0
            elif event.__dict__['key'] == pygame.K_DOWN:
                guy.move(1, screen)
                action = 0
            elif event.__dict__['key'] == pygame.K_RIGHT:
                guy.move(2, screen)
                action = 0
            elif event.__dict__['key'] == pygame.K_LEFT:
                guy.move(0, screen)
                action = 0
    if action:
        guy.move(guy.curr_dir, screen)
    ghost1.find_targ(*guy.get_coords())
    ghost1.render_loc_ghost(screen)

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()