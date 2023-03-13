import pygame
from pygame.locals import *
from states.gamestate import *
from main import * 
import random


class Runner(GameState):
    def __init__(self,display_surf,size,config):
        super().__init__(display_surf,size)
        self._config = config

        self._finishX = 0
        self._finishY = 0
        self._initialX = 0
        self._initialY = 0
        self._create_visual_matrix()
        self.maze = self.generate_maze(self._config['game']['matrix_size'],self._config['game']['matrix_size'])
        
        self.block_position = [self._initialX, self._initialY] # The position of the block in the maze
    
       
        for i in self.maze:
         print('\t'.join(map(str, i)))
         
    def _create_visual_matrix(self):
        self._width = self._size[0]
        self._height = self._size[1]
        self._rows = self._config['game']['matrix_size']
        self._cols = self._config['game']['matrix_size']
        self._square_width = self._width / self._cols
        self._square_height = self._height / self._rows
        
    def display(self):
        self._display_surf.fill((colors['BLACK']))

        # Create the matrix of squares
        for row in range(self._rows):
            for col in range(self._cols):
                # Calculate the position of the square
                x = col * self._square_width + self._config['visual']['block_margin']
                y = row * self._square_height + self._config['visual']['block_margin']
                
                # Get the color of the square
                if self.maze[row][col] == 0:
                    color = colors['BLACK']
                else:
                    color = colors['WHITE']
                
                # Draw the square
                pygame.draw.rect(self._display_surf, color, (x, y, self._square_width-self._config['visual']['block_margin']*2, self._square_height-self._config['visual']['block_margin']*2))

                # Draw the block
                if [row, col] == self.block_position:
                    pygame.draw.rect(self._display_surf, colors['RED'], (x, y, self._square_width-self._config['visual']['block_margin']*2, self._square_height-self._config['visual']['block_margin']*2))
                padding =0 
                # Draw the start cell as X and finish cell as O
                if (row, col) == (0, 0):
                    font = pygame.font.Font(None, int(self._square_height*0.8))
                    text = font.render('X', True, colors['GREEN'])
                    text_rect = text.get_rect(center=(int(x+self._square_width/2), int(y+self._square_height/2)))
                    self._display_surf.blit(text, text_rect)
                elif (row, col) == (self._rows-1, self._cols-1):
                    font = pygame.font.Font(None, int(self._square_height*0.8))
                    text = font.render('O', True, colors['GREEN'])
                    text_rect = text.get_rect(center=(int(x+self._square_width/2), int(y+self._square_height/2)))
                    self._display_surf.blit(text, text_rect)

    def generate_maze(self, width, height):
        # Create a 2D grid with all walls intact
        maze = [[0] * width for _ in range(height)]

        # Choose a random finishing line
        self._finishX  = random.randint(height-2, height-1)
        self._finishY = random.randint(0, width-1)
     
        # Call the recursive backtracking algorithm to carve a path through the maze
       # self.carve_path(self._finishX, self._finishY, maze)
        maze = self.generate(maze)
       
        return maze
        
    
    def carve_path(self, row, col, maze):
    # Mark the current cell as visited
        maze[row][col] = 1

    # Create a list of unvisited neighbors
        neighbors = []
        if row > 0 and maze[row-1][col] == 0:
            neighbors.append((row-1, col))
        if row < len(maze)-1 and maze[row+1][col] == 0:
            neighbors.append((row+1, col))
        if col > 0 and maze[row][col-1] == 0:
            neighbors.append((row, col-1))
        if col < len(maze)-1 and maze[row][col+1] == 0:
            neighbors.append((row, col+1))

        # Randomly select an unvisited neighbor
        if neighbors:
            next_row, next_col = random.choice(neighbors)

            # Carve a path to the neighbor
            if next_row < row:
                maze[row-1][col] = 1
            elif next_row > row:
                maze[row+1][col] = 1
            elif next_col < col:
                maze[row][col-1] = 1
            elif next_col > col:
                maze[row][col+1] = 1

            # If the neighbor is the start or end point, mark it in the maze
            if (next_row, next_col) == (self._initialX, self._initialY):
                maze[next_row][next_col] = 2
                print("initial")
            elif (next_row, next_col) == (self._finishX, self._finishY):
                maze[next_row][next_col] = 3
                print("finish")

            # Recursively carve paths from the neighbor
            self.carve_path(next_row, next_col, maze)


    def generate(self, maze):
        # Start carving paths from the bottom-right corner
        self.carve_path(self._initialX, self._initialY, maze)

        # Fix the start and finish points in the maze
        maze[self._initialX][self._initialY] = 2
        maze[self._finishX][self._finishY] = 3

        return maze