import pygame
from pygame.locals import *
from states.gamestate import *
from states.block import *
from main import * 
import random

class Player():
    def __init__(self,maze, initial_position) -> None:
        self._block_state = BlockState(initial_position[0],initial_position[1],False,None)
        self._maze = maze
        self._printCurrentState()
        self._printChildStates()
    
    def getMoves(self):
        return self._block_state.child_block_states(self._maze)
    
    def _printCurrentState(self):
        print("Current state : \n")
        print(str(self._block_state))
        print(self.maze[self._block_state.x])
        
        print("\n")
    
    def _printChildStates(self):
        print("Available Moves : \n")
        moves = self.getMoves()
        for x in range(len(moves)):
            print (moves[x][0] + ',' + str(moves[x][1]))