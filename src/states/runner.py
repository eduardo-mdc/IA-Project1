import pygame
from pygame.locals import *
from states.gamestate import *
from main import * 

class Runner(GameState):
    def __init__(self,display_surf,size,config):
        super().__init__(display_surf,size)
        self._config = config
        self._create_visual_matrix()
        
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
        
