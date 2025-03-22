import pygame 

class Guy:
    directions = [-5, 5, 5, -5] # left, bottom, right, top
    normal_directions = {'left': (0, -1), 'right': (0, 1), 'top': (-1, 0), 'bottom': (1, 0)}
    simple_dirs =  {'left': 0, 'right': 2, 'up': 3, 'down': 1}
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
        self.size = 9
        self.curr_loc = (50, 50)
        self.board_size = board_size
        self.board_left = board_left
        self.cell_size = cell_size
        self.curr_dir = None
        self.move_len = 5
        self.board_edge = (self.board_left[0] + self.board_size[0] * self.cell_size, self.board_left[1] + self.board_size[1] * self.cell_size)
        top_left = (self.board_left[0] - self.board_size[0] * self.cell_size, self.board_left[1] - self.board_size[1] * self.cell_size)
        top_right = (top_left[0] + board_size[0] * cell_size, top_left[1])
        bottom_right = (top_right[0], top_right[1] - self.board_size[1] * self.cell_size)
        bottom_left = (top_left[0], bottom_right[1])

        corners = {'top left': top_left, 'bottom right': bottom_right, 'bottom left': bottom_left, 'top right': top_right}

    def set_speed(self, v):
        self.move_len = v
        self.directions = [-v, v, v, -v]


    def get_cell(self, char_pos):
        if char_pos[0] >= self.board_left[0] and char_pos[0] <= self.board_left[0] + self.cell_size * self.board_size[0] and char_pos[1] >= self.board_left[1] and char_pos[1] <= self.board_left[1] + self.cell_size * self.board_size[1]:
            x = char_pos[0] - self.board_left[0]
            y = char_pos[1] - self.board_left[1]
            a = min(x // self.cell_size, self.board_size[0]-1)
            b = min(y // self.cell_size, self.board_size[1]-1)
            if x % self.cell_size == 0 and self.table[b][a] == self.obstacle:
                return (max(int(a) - 1, 0), int(b))
            elif y % self.cell_size == 0 and self.table[b][a] == self.obstacle:
                (int(a), max(int(b) - 1, 0))
            return (int(a), int(b))

    def change_loc(self, dir_0):
        self.curr_dir = dir_0
        a, b = self.curr_loc
        if dir_0 == 0 or dir_0 == 2:
            if self.directions[dir_0] < 0:
                m = - self.size
            else:
                m = self.size
            next_loc = (min(max(0, a + self.directions[dir_0]), self.board_left[0]+self.board_size[0]*self.cell_size), b)
            loc_edge = (min(max(0, a + m + self.directions[dir_0]), self.board_left[0]+self.board_size[0]*self.cell_size), b + self.size)
            loc_edge2 = (min(max(0, a + m + self.directions[dir_0]), self.board_left[0]+self.board_size[0]*self.cell_size), b - self.size)
            cell = self.get_cell(loc_edge)
            cell2 = self.get_cell(loc_edge2)
            if self.table[cell[1]][cell[0]] == self.obstacle:
                pass
            elif self.table[cell2[1]][cell2[0]] == self.obstacle:
                pass
            else:
                self.curr_loc = next_loc
        elif dir_0 == 1 or dir_0 == 3:
            if self.directions[dir_0] < 0:
                m = - self.size
            else:
                m = self.size
            next_loc = (a, min(max(0, b + self.directions[dir_0]), self.board_left[1]+self.board_size[1]*self.cell_size))
            loc_edge = (a + self.size, min(max(0, b + m + self.directions[dir_0]), self.board_left[1]+self.board_size[1]*self.cell_size))
            loc_edge2 = (a - self.size, min(max(0, b + m + self.directions[dir_0]), self.board_left[1]+self.board_size[1]*self.cell_size))
            cell = self.get_cell(loc_edge)
            cell2 = self.get_cell(loc_edge2)
            if self.table[cell[1]][cell[0]] == self.obstacle:
                pass
            elif self.table[cell2[1]][cell2[0]] == self.obstacle:
                pass
            else:
                self.curr_loc = next_loc

    def render_loc(self, screen):
        pygame.draw.circle(screen, pygame.Color('yellow'), self.curr_loc, self.size)

    def move(self, dir, screen):
        self.change_loc(dir)
        self.render_loc(screen)
        #print(self.curr_loc)

    def get_coords(self):
        return self.curr_loc
    
    def is_obstacle(self, val):
        if val != self.obstacle:
            return False
        return True

    def temp_board_render(self, screen):
        for y in range(self.board_size[1]):
            for x in range(self.board_size[0]):
                if self.table[y][x] == self.obstacle:
                    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(self.board_left[0] + self.cell_size * x, self.board_left[1] + self.cell_size * y, self.cell_size, self.cell_size), 1)
                        