import pygame
from pygame.locals import *
from states.gamestate import *
from states.block import *
from main import * 
import random

class Player():
    def __init__(self,maze) -> None:
        self._block_state = BlockState(0,0,False,None)
        self._maze = maze
    
    def getMoves(self):
        self._block_state.child_block_states(self._maze)