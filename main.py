import pygame, sys
from basecharacter import Guy
from points import Point
from blinkychar import Blinky

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("ubuntumono", 30)
game_over_font = pygame.font.SysFont("dejavusansmono", 48)
text_color = pygame.Color("crimson")
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#game creation
guy = Guy((31, 15), 30, (0, 0))
guy.render_loc(screen)
points = Point((31, 15), 30, (0, 0))
points.render(screen)

ghost1 = Blinky((31, 15), 30, (0, 0))
ghost1.render_loc_ghost(screen)
ghost1.set_speed(2)

score = 0


def show_score(self, score):
    score = font.render(f'{score}', True, text_color)
    screen.blit(score, (400, 500))


while running:
    screen.fill("black")
    action = 1
    guy.temp_board_render(screen)
    points.render(screen)
    score += points.eat_point(guy.curr_loc)
    show_score(screen, score)
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
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
