# clyde
import pygame
from blinkychar import Blinky


class Clyde(Blinky):
    def __init__(self, board_size, cell_size, board_left, table=0):
        super().__init__(board_size, cell_size, board_left, table)
        self.curr_loc = (26 * 30 + 15, 13 * 30 + 15)
        self.chase_radius = 200

    def change_radius(self, r):
        self.chase_radius = r

    def chase(self, pac_loc):
        if ((self.curr_loc[0] - pac_loc[0]) ** 2 + (self.curr_loc[1] - pac_loc[1]) ** 2) ** 0.5 >= self.chase_radius:
            self.find_targ(*pac_loc)
        else:
            self.find_targ(self.board_left[0] + int(self.cell_size * 1.5), self.board_edge[1] - int(1.5 * self.cell_size))