import pygame 

class Guy:
    dir = [-5, 5, 5, -5] # left, top, right, bottom
    table = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['2', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '2'] ,
                    ['1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
    def __init__(self, board_size, cell_size, board_left, table=0):
        self.obstacle = '1'
        self.size = 10
        self.curr_loc = (50, 50)
        self.board_size = board_size
        self.board_left = board_left
        self.cell_size = cell_size
        self.curr_dir = None

    def get_cell(self, char_pos):
        if char_pos[0] >= self.board_left[0] and char_pos[0] <= self.board_left[0] + self.cell_size * self.board_size[0] and char_pos[1] >= self.board_left[1] and char_pos[1] <= self.board_left[1] + self.cell_size * self.board_size[1]:
            x = char_pos[0] - self.board_left[0]
            y = char_pos[1] - self.board_left[1]
            return (int(min(x // self.cell_size, self.board_size[0]-1)), int(min(y // self.cell_size, self.board_size[1]-1)))

    def change_loc(self, dir):
        self.curr_dir = dir
        a, b = self.curr_loc
        if dir == 0 or dir == 2:
            if self.dir[dir] < 0:
                m = - self.size // 2
            else:
                m = self.size // 2
            next_loc = (min(max(0, a + self.dir[dir]), self.board_left[0]+self.board_size[0]*self.cell_size), b)
            loc_edge = (min(max(0, a + m + self.dir[dir]), self.board_left[0]+self.board_size[0]*self.cell_size), b)
            cell = self.get_cell(loc_edge)
            if self.table[cell[1]][cell[0]] == self.obstacle:
                pass
            else:
                self.curr_loc = next_loc
        elif dir == 1 or dir == 3:
            if self.dir[dir] < 0:
                m = - self.size // 2
            else:
                m = self.size // 2
            next_loc = (a, min(max(0, b + self.dir[dir]), self.board_left[1]+self.board_size[1]*self.cell_size))
            loc_edge = (a, min(max(0, b + m + self.dir[dir]), self.board_left[1]+self.board_size[1]*self.cell_size))
            cell = self.get_cell(loc_edge)
            if self.table[cell[1]][cell[0]] == self.obstacle:
                pass
            else:
                self.curr_loc = next_loc

    def render_loc(self, screen):
        pygame.draw.circle(screen, pygame.Color('yellow'), self.curr_loc, self.size)

    def move(self, dir, screen):
        self.change_loc(dir)
        self.render_loc(screen)

    def temp_board_render(self, screen):
        for y in range(self.board_size[1]):
            for x in range(self.board_size[0]):
                if self.table[y][x] == self.obstacle:
                    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(self.board_left[0] + self.cell_size * x, self.board_left[1] + self.cell_size * y, self.cell_size, self.cell_size), 1)