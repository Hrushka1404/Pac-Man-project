# inky ghost
import pygame
from blinkychar import Blinky


class Inky(Blinky):
    def __init__(self, board_size, cell_size, board_left, table=0):
        super().__init__(board_size, cell_size, board_left, table)
        self.curr_loc = (27 * 30 + 15, 13 * 30 + 15)

    def chase(self, pac_loc, blinky_loc, direc):
        m = 0
        n = 0
        if direc == 0 or direc == 2:
            m = self.directions[direc]
        elif direc is None:
            m = -5
        else:
            n = self.directions[direc]
        new_loc = (pac_loc[0] + m, pac_loc[1] + n)
        final_loc = self.mirror(blinky_loc, new_loc)
        if final_loc[0] >= 0 and final_loc[0] <= self.board_size[0] * self.cell_size and final_loc[1] >= 0 and final_loc[1] <= self.board_size[1] * self.cell_size:
            self.find_targ(*final_loc)
        else:
            self.find_targ(*pac_loc)

    def mirror(self, loc, base_loc):
        x = 2 * base_loc[0] - loc[0]
        y = 2 * base_loc[1] - loc[1]
        return (x, y)