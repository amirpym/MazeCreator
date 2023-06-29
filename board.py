import pygame
import random

class Board:
    def __init__(self, height, width, window) -> None:
        self.path = []
        self.done = False
        self.first = True
        self.height = height
        self.out_coords = ()
        self.width = width
        wall = True
        self.window = window
        self.cube_size = 20
        self.board_visualization = {}
        self.cell_index = {}
        self.start_board = 100
        self.key_point = (0,0)
        row, col = 0, 0
        for h in range(self.start_board,self.height - self.start_board,self.cube_size):
            for w in range(self.start_board,self.width - self.start_board, self.cube_size):
                self.board_visualization[(w + self.cube_size/2, h+ self.cube_size/2)] = [wall,wall,wall,wall]
                self.cell_index[(row, col)] = (w + self.cube_size/2, h+ self.cube_size/2)
                col += 1
            row += 1
            col = 0
        self.rows = row
    def draw_board(self):
        
        for key in self.board_visualization.keys():
            if self.board_visualization[key][0]:
                coords = tuple(key)
                pygame.draw.line(self.window, (100, 50, 70),
                 [coords[0] - self.cube_size/2, coords[1] - self.cube_size/2],
                 [coords[0] - self.cube_size/2, coords[1] + self.cube_size/2], 2)
 
            if self.board_visualization[key][1]:
                coords = tuple(key)
                pygame.draw.line(self.window, (100, 50, 70),
                 [coords[0] - self.cube_size/2, coords[1] - self.cube_size/2],
                 [coords[0] + self.cube_size/2, coords[1] - self.cube_size/2], 2)
                    
            if self.board_visualization[key][2]:
                coords = tuple(key)
                pygame.draw.line(self.window, (100, 50, 70),
                 [coords[0] + self.cube_size/2, coords[1] - self.cube_size/2],
                 [coords[0] + self.cube_size/2, coords[1] + self.cube_size/2], 2)
            
            if self.board_visualization[key][3]:
                coords = tuple(key)
                pygame.draw.line(self.window, (100, 50, 70),
                 [coords[0] - self.cube_size/2, coords[1] + self.cube_size/2],
                 [coords[0] + self.cube_size/2, coords[1] + self.cube_size/2], 2)
        pygame.draw.rect(self.window, (70, 70, 70),[self.cell_index[(self.rows -3, self.rows -1)][0] - self.cube_size/2,self.cell_index[(self.rows -3, self.rows -1)][1] -self.cube_size/2,self.cube_size, self.cube_size ], 0)

        
    def update_wall_status(self, row_ind, column_ind, wall_index):
        if wall_index == 0:
            self.board_visualization[self.cell_index[(row_ind, column_ind)]][wall_index] = False
            try:
                self.board_visualization[self.cell_index[(row_ind, column_ind -1)]][wall_index - 2] = False
            except:
                pass
        if wall_index == 1:
            self.board_visualization[self.cell_index[(row_ind, column_ind)]][wall_index] = False
            try:
                self.board_visualization[self.cell_index[(row_ind - 1, column_ind)]][wall_index -2] = False
            except:
                pass
        if wall_index == 2:
            self.board_visualization[self.cell_index[(row_ind, column_ind)]][wall_index] = False
            try:
                self.board_visualization[self.cell_index[(row_ind, column_ind + 1)]][wall_index -2] = False
            except:
                pass
        if wall_index == 3:
            self.board_visualization[self.cell_index[(row_ind, column_ind)]][wall_index] = False
            try:
                self.board_visualization[self.cell_index[(row_ind + 1, column_ind)]][wall_index -2] = False
            except:
                pass

    def draw_maze_runner(self, runner_movement):
        coords = self.cell_index[runner_movement.coords]
        prev_coords = self.cell_index.get(runner_movement.previous_coords)
        if prev_coords is not None:
            pygame.draw.rect(self.window, (255, 255, 255),
                    [prev_coords[0] - self.cube_size/2,prev_coords[1] -self.cube_size/2,self.cube_size, self.cube_size ], 0)
        pygame.draw.rect(self.window, (255, 255, 255),
                 [coords[0] - self.cube_size/2,coords[1] -self.cube_size/2,self.cube_size, self.cube_size ], 0)

    def maze_runner_road(self,runner):
        if list(self.board_visualization.values()).count([True, True, True, True]) == 0:
            self.done = True
        options = []
        options = [(runner.coords[0]-1, runner.coords[1]),(runner.coords[0]+1, runner.coords[1]),(runner.coords[0], runner.coords[1]-1), (runner.coords[0], runner.coords[1]+1)]
        try:
            options.remove(runner.previous_coords)
        except:
            pass
        c = tuple(options)
        prev_coord = runner.coords
        for coord in c:
            try:
                if self.board_visualization[self.cell_index[coord]] != [True,True,True, True]:
                    options.remove(coord)
                else:
                    self.key_point = prev_coord
            except:
                options.remove(coord)
        try:
            new_coord = random.choice(options)
            options.remove(new_coord)
        except: 
            try:
                runner.coords = self.path[-2]

                self.path.pop(-2)
                return
            except:
                return
        runner.coords = new_coord

        runner.previous_coords = prev_coord
        result = tuple(a - b for a, b in zip(new_coord, prev_coord))
        if result == (0, 1):
            index = 0
        elif result == (0, -1):
            index = 2
        elif result == (1, 0):
            index = 1
        elif result == (-1, 0):
            index = 3
        self.update_wall_status(runner.coords[0], runner.coords[1], index)
        self.path.append(runner.coords)
        