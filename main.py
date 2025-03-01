import pygame, sys
from boardScript import Board
from world import World
from basecharacter import Guy
from points import Point

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#game creation
playboard = Board(screen)
playboard.board_render(screen)
guy = Guy((31, 15), 30, (0, 0))
guy.render_loc(screen)
points = Point((31, 15), 30, (0, 0))
points.render(screen)


while running:
    screen.fill("black")
    action = 1
    guy.temp_board_render(screen)
    points.render(screen)
    points.eat_point(guy.curr_loc)
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
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()