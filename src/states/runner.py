import pygame
from pygame.locals import *
from states.gamestate import *
from main import * 
import random


class Runner(GameState):
    def __init__(self,display_surf,size,config):
        super().__init__(display_surf,size)
        self._config = config
        self._create_visual_matrix()
        self.generate_maze(self._config['game']['matrix_size'],self._config['game']['matrix_size'])
       
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
                color = colors['LAVENDER']
                
                # Draw the square
                pygame.draw.rect(self._display_surf, color, (x, y, self._square_width-self._config['visual']['block_margin']*2, self._square_height-self._config['visual']['block_margin']*2))

   
    def generate_maze(self, width, height):
        # Create a 2D grid with all walls intact
        maze = [[0] * width for _ in range(height)]

        # Choose a random finishing line
        finish_row = random.randint(height//2, height-2)
        finish_col = width - 1

        # Call the recursive backtracking algorithm to carve a path through the maze
        self.carve_path(0, 0, finish_row, finish_col, maze)

        # Remove the walls at the entrance and exit
        maze[0][0:2] = [1, 1]
        maze[finish_row][finish_col-1:finish_col+1] = [1, 1]

        for row in range(height):
            print(*maze[row])

        return maze

    def carve_path(self, row, col, finish_row, finish_col, maze):
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
        if col < len(maze[0])-1 and maze[row][col+1] == 0:
            neighbors.append((row, col+1))

        # If there are no unvisited neighbors, backtrack
        if not neighbors:
            return

        # Choose a random unvisited neighbor
        n_row, n_col = random.choice(neighbors)

        # Remove the wall between the current cell and the chosen neighbor
        if n_row < row:
            maze[row][col] &= ~0b1000 # remove North wall
            maze[n_row][n_col] &= ~0b0010 # remove South wall
        elif n_row > row:
            maze[row][col] &= ~0b0010 # remove South wall
            maze[n_row][n_col] &= ~0b1000 # remove North wall
        elif n_col < col:
            maze[row][col] &= ~0b0100 # remove West wall
            maze[n_row][n_col] &= ~0b0001 # remove East wall
        elif n_col > col:
            maze[row][col] &= ~0b0001 # remove East wall
            maze[n_row][n_col] &= ~0b0100 # remove West wall

        # Check if the chosen neighbor is next to the finishing line
        if (n_row == finish_row and n_col == finish_col-1) or (n_row == finish_row-1 and n_col == finish_col-1):
            # If the neighbor is next to the finishing line, remove the wall between them and finish carving the path
            if n_row < row:
                maze[n_row][n_col] &= ~0b0010 # remove South wall
            elif n_row > row:
                maze[n_row][n_col] &= ~0b1000 # remove

        # Recursively carve a path through the neighbor
        self.carve_path(n_row, n_col, finish_row,finish_col,maze)