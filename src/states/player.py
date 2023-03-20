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
        self._printChildStates()
    
    def getMoves(self):
        return self._block_state.child_block_states(self._maze)

    def process_move(self, move, arrow):
        if arrow == "left":
            match move:
                case "fall_l":
                    self._block_state = self._block_state.fall_l(self._maze)
                case "get_up_l":
                    self._block_state = self._block_state.get_up_l(self._maze)
                case "roll_l":
                    self._block_state = self._block_state.roll_l(self._maze)

        elif arrow == "right":
            match move:
                case "fall_r":
                    self._block_state = self._block_state.fall_r(self._maze)
                case "get_up_r":
                    self._block_state = self._block_state.get_up_r(self._maze)
                case "roll_r":
                    self._block_state = self._block_state.roll_r(self._maze)

        elif arrow == "down":
            match move:
                case "fall_d":
                    self._block_state = self._block_state.fall_d(self._maze)
                case "get_up_d":
                    self._block_state = self._block_state.get_up_d(self._maze)
                case "roll_d":
                    self._block_state = self._block_state.roll_d(self._maze)

        elif arrow == "up":
            match move:
                case "fall_u":
                    self._block_state = self._block_state.fall_u(self._maze)
                case "get_up_u":
                    self._block_state = self._block_state.get_up_u(self._maze)
                case "roll_u":
                    self._block_state = self._block_state.roll_u(self._maze)

    
    def _printChildStates(self):
        print("Available Moves : \n")
        moves = self.getMoves()
        for x in range(len(moves)):
            print (moves[x][0] + ',' + str(moves[x][1]))