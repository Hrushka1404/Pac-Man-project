import pygame, sys
from basecharacter import Guy
from points import Point
from blinkychar import Blinky
from time import sleep
from pinkychar import Pinky
from inkychar import Inky
from clydechar import Clyde

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("ubuntumono", 30)
game_over_font = pygame.font.SysFont("dejavusansmono", 48)
text_color = pygame.Color("crimson")
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

big_font = pygame.font.SysFont('boulder', 350)

#game creation
guy = Guy((31, 15), 30, (0, 0))
guy.render_loc(screen)
points = Point((31, 15), 30, (0, 0))
points.render(screen)

ghost1 = Blinky((31, 15), 30, (0, 0))
ghost1.render_loc_ghost(screen)
ghost1.set_speed(3)

ghost2 = Pinky((31, 15), 30, (0, 0))
ghost2.render_loc_ghost(screen, 'pink')
ghost2.set_speed(3)

ghost3 = Inky((31, 15), 30, (0, 0))
ghost3.render_loc_ghost(screen, 'cyan')
ghost3.set_speed(3)

ghost4 = Clyde((31, 15), 30, (0, 0))
ghost4.render_loc_ghost(screen, 'orange')
ghost4.set_speed(3)


score = 0


def show_score(self, score):
    score = font.render(f'{score}', True, text_color)
    screen.blit(score, (400, 500))

def show_game_over():
    text = big_font.render('GAME OVER', True, 'red')
    screen.blit(text, (0, 0))


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

    ghost2.chase(*guy.get_coords(), guy.curr_dir)
    ghost2.render_loc_ghost(screen, 'pink')

    ghost3.chase(guy.get_coords(), ghost1.get_coords(), guy.curr_dir)
    ghost3.render_loc_ghost(screen, 'cyan')

    ghost4.chase(guy.get_coords())
    ghost4.render_loc_ghost(screen, 'orange')

    state = (ghost1.pac_caught(guy.curr_loc) or ghost2.pac_caught(guy.curr_loc))
    if state:
        show_game_over()

    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()
