import pygame
from pygame.locals import *
from states.gamestate import *
from states.player import *
from main import * 
from generator import *


class Visualizer(GameState):
    def __init__(self,display_surf,size,start,end,matrix_size,matrix,moves):
        super().__init__(display_surf,size)


        print("----------VISUALIZER----------------")
        self._size = size
        self._init_visual(matrix_size)
    
        self.maze = matrix
        print_matrix(self.maze,matrix_size)

        self.player = Player(self.maze,start,self._display_surf)
        self.inputs = moves.get_parents()
        self.move_counter = 0

       
         
    def _init_visual(self,matrix_size):
        self._width = self._size[0]
        self._height = self._size[1]
        self._rows = matrix_size
        self._cols = matrix_size
        self._square_width = self._width / self._cols
        self._square_height = self._height / self._rows

        self.tile_image = pygame.image.load('src/artset/grass_tile.png')
        self.void_image = pygame.image.load('src/artset/water_tile.png')
        self.end_image = pygame.image.load('src/artset/end_tile.png')

        self.player_h = pygame.image.load('src/artset/player_horizontal.png')
        self.player_v = pygame.image.load('src/artset/player_vertical.png')
        
    def display(self):
        self._display_surf.fill(((0,0,0)))

        # Create the matrix of squares
        for row in range(self._rows):
            for col in range(self._cols):
                # Calculate the position of the square
                x = col * self._square_width
                y = row * self._square_height
                
               # Get the color of the square
                if self.maze[row][col] == 0:
                    scaled_image = pygame.transform.scale(self.void_image, (self._square_width, self._square_height))
                elif (row, col) == (self._rows-1, self._cols-1):
                    scaled_image = pygame.transform.scale(self.end_image, (self._square_width, self._square_height))
                else:
                    scaled_image = pygame.transform.scale(self.tile_image, (self._square_width, self._square_height))
                self._display_surf.blit(scaled_image, (x, y))

        self.player.display(self._square_width,self._square_height)
        
    def add_input(self, input):
        self.inputs.append(input)

    def process_input(self):
        self.player._block_state = self.inputs[self.move_counter]
        self.move_counter += 1
        