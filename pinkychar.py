# pinky
import pygame
from blinkychar import Blinky

class Pinky(Blinky):
    def __init__(self, board_size, cell_size, board_left, table=0):
        super().__init__(board_size, cell_size, board_left, table)
        self.curr_loc = (28 * 30 + 15, 13 * 30 + 15)

    def chase(self, x, y, direc):
        m = 0
        n = 0
        if direc == 0 or direc == 2:
            m = self.directions[direc]
        elif direc is None:
            m = -5
        else:
            n = self.directions[direc]
        self.find_targ(x + 2 * m, y + 2 * n)
