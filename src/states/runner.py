import pygame
from pygame.locals import *
from states.gamestate import *

class Runner(GameState):
    def __init__(self,display_surf,size):
        super().__init__(display_surf,size)