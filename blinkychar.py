from basecharacter import Guy
import pygame
from collections import deque


class Blinky(Guy):
    def __init__(self, board_size, cell_size, board_left, table=0):
        super().__init__(board_size, cell_size, board_left, table=0)
        self.curr_loc = (29 * 30 + 15, 13 * 30 + 15)
        self.curr_dir = 3

    def get_step(self, x, y):
        targ_cell = self.get_cell((x, y))[::-1]
        my_cell = self.get_cell(self.curr_loc)[::-1]

        a, b = self.curr_loc

        rows = len(self.table)
        cols = len(self.table[0])

        doub_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        word_dirs = ['up', 'down', 'left', 'right']
        queue = deque([(my_cell[0], my_cell[1], None)])
        visited = set((my_cell[0], my_cell[1]))
        
        while queue:
            curr_row, curr_col, first_move = queue.popleft()

            if (curr_row, curr_col) == targ_cell:
                return first_move
            
            for i, (u, r) in enumerate(doub_directions):
                new_row, new_col = curr_row + u, curr_col + r

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and not self.is_obstacle(self.table[new_row][new_col])
                    and (new_row, new_col) not in visited 
                ):
                    visited.add((new_row, new_col))

                    if first_move is None:
                        next_frst_move = word_dirs[i]
                    else:
                        next_frst_move = first_move
                    queue.append((new_row, new_col, next_frst_move))
        return None
         

    def find_targ(self, x, y):
        direction = self.get_step(x, y)
        if direction:
            num_dir = self.simple_dirs[direction]
            a, b = self.get_cell(self.curr_loc)
            x1, y1 = self.curr_loc
            if direction == 'left' or direction == 'right':
                if y1 == b * self.cell_size + self.cell_size//2 + self.board_left[1]:
                    self.change_loc(num_dir)
                else:
                    self.change_loc(self.curr_dir)
            else:
                if x1 == a * self.cell_size + self.cell_size//2 + self.board_left[0]:
                    self.change_loc(num_dir)
                else:
                    self.change_loc(self.curr_dir)
        else:
            print(direction)


    def render_loc_ghost(self, screen):
        pygame.draw.circle(screen, pygame.Color('red'), self.curr_loc, self.size)

        

