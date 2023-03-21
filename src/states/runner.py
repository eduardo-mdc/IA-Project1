import pygame
from pygame.locals import *
from states.gamestate import *
from states.player import *
from main import * 
import random


class Runner(GameState):
    def __init__(self,display_surf,size,config):
        super().__init__(display_surf,size)
        self._config = config
        self.tile_image = pygame.image.load('src/artset/grass_tile.png')
        self.void_image = pygame.image.load('src/artset/water_tile.png')
        self.end_image = pygame.image.load('src/artset/end_tile.png')

        self.player_h = pygame.image.load('src/artset/player_horizontal.png')
        self.player_v = pygame.image.load('src/artset/player_vertical.png')

        self._finishX = 0
        self._finishY = 0
        self._initialX = 0
        self._initialY = 0
        self._create_visual_matrix()

        size = self._config['game']['matrix_size']
        start = (0, 0)
        end = (size-1, size-1)
        dead_end_prob = 0.2

        self.maze = generate_matrix(size, start, end, dead_end_prob)
        print_matrix(self.maze,size)
        self.block_position = [self._initialX, self._initialY] # The position of the block in the maze
        self.player = Player(self.maze,self.block_position)
        self.inputs = []
       
    def _display_player():
        pass
    
         
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
                    self._display_surf.blit(self.void_image, (x, y))
                    # Draw the PNG tile
                    pass
                else:
                    self._display_surf.blit(self.tile_image, (x, y))
            
                    
                # Draw the square
                #  pygame.draw.rect(self._display_surf, color, (x, y, self._square_width-self._config['visual']['block_margin']*2, self._square_height-self._config['visual']['block_margin']*2))

                # Draw the block
                if [row, col] == self.block_position:
                    pygame.draw.rect(self._display_surf, colors['RED'], (x, y, self._square_width-self._config['visual']['block_margin']*2, self._square_height-self._config['visual']['block_margin']*2))

                # Draw the start cell as X and finish cell as O
                if (row, col) == (0, 0):
                    self._display_surf.blit(self.player_v, (x, y))
                elif (row, col) == (self._rows-1, self._cols-1):
                    self._display_surf.blit(self.end_image, (x, y))
        
    def add_input(self, input):
        self.inputs.append(input)

    def process_input(self):
        moves = self.player.getMoves()
        if len(self.inputs) != 0:
            arrow = self.inputs.pop()
            for move in moves:
                self.player._block_state.process_move(move, arrow)

def generate_matrix(size, start, end, dead_end_prob=0.7):
    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Set the starting and ending points
    i, j = start
    matrix[i][j] = 8
    i, j = end
    matrix[i][j] = 9

    # Generate random dead ends in the matrix
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                continue
            if random.random() < dead_end_prob:
                matrix[i][j] = 0

    # Generate a solution path from start to end
    path = [(start[0], start[1])]
    i, j = start
    while (i, j) != end:
        # Find the neighboring cells that are not dead ends or part of the path
        neighbors = []
        if i > 0 and matrix[i-1][j] not in (1, 2):
            neighbors.append((i-1, j))
        if j > 0 and matrix[i][j-1] not in (1, 2):
            neighbors.append((i, j-1))
        if i < size-1 and matrix[i+1][j] not in (1, 2):
            neighbors.append((i+1, j))
        if j < size-1 and matrix[i][j+1] not in (1, 2):
            neighbors.append((i, j+1))
        # Choose a random neighbor and mark it as part of the path
        if neighbors:
            i, j = random.choice(neighbors)
            path.append((i, j))
            # Mark the cell as part of the path, unless it's the starting or ending point
            if (i, j) != start and (i, j) != end:
                matrix[i][j] = 1
        # If there are no neighbors available, backtrack to the previous cell
        else:
            i, j = path[-1]
            path.pop()

    return matrix


def print_matrix(matrix,size):
    print("Game Matrix")
    
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print('\n')