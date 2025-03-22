import pygame

class Point:
    table = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'B', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1'] ,
                    ['1', 'B', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['2', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '2'] ,
                    ['1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '1', '1', '1', '1', '0', '0', 'B', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'] ,
                    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'] ,
                    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
    def __init__(self, board_size, cell_size, board_left, table=0):
        self.board_size = board_size
        self.cell_size = cell_size
        self.board_left = board_left
        self.is_eaten = [[1 for j in range(board_size[0])] for i in range(board_size[1])]


    def render(self, screen):
        for i in range(self.board_size[1]):
            for j in range(self.board_size[0]):
                if self.table[i][j] == '0' and self.is_eaten[i][j] == 1:
                    curr_loc = (self.board_left[1] + (j) * self.cell_size + self.cell_size // 2, self.board_left[0] + (i) * self.cell_size + self.cell_size // 2)
                    pygame.draw.circle(screen, pygame.Color('white'), curr_loc, self.cell_size // 6)
                if self.table[i][j] == "B" and self.is_eaten[i][j] == 1:
                    curr_loc = (self.board_left[1] + (j) * self.cell_size + self.cell_size // 2, self.board_left[0] + (i) * self.cell_size + self.cell_size // 2)
                    pygame.draw.circle(screen, pygame.Color('white'), curr_loc, self.cell_size // 2)

    def get_cell(self, char_pos):
        if char_pos[0] >= self.board_left[0] and char_pos[0] <= self.board_left[0] + self.cell_size * self.board_size[0] and char_pos[1] >= self.board_left[1] and char_pos[1] <= self.board_left[1] + self.cell_size * self.board_size[1]:
            x = char_pos[0] - self.board_left[0]
            y = char_pos[1] - self.board_left[1]
            return (int(min(x // self.cell_size, self.board_size[0]-1)), int(min(y // self.cell_size, self.board_size[1]-1)))

    def eat_point(self, pac_coord):
        x, y = self.get_cell(pac_coord)
        if x > self.board_size[0] - 1 or y > self.board_size[1] - 1:
            return 0
        if self.is_eaten[y][x] == 1:
            ans = 1
        else:
            ans = 0
        self.is_eaten[y][x] = 0
        return ans


    def eat_big_point(self, pac_coord):
        x, y = self.get_cell(pac_coord)
        if x > self.board_size[0] - 1 or y > self.board_size[1] - 1:
            return "basic"
        if self.is_eaten[y][x] == 1:
            ans = "scared"
        else:
            ans = "basic"
        self.is_eaten[y][x] = 0
        return ans

