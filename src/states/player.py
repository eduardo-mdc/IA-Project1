import pygame
from pygame.locals import *
from states.gamestate import *
from states.block import *
from main import * 
import random

class Player():
    def __init__(self,maze,initial_position,display_surf) -> None:
        self._block_state = BlockState(initial_position[0],initial_position[1],False,None)
        self._maze = maze
        self._printChildStates()
        self._display_surf = display_surf
        self._vertical_tile = pygame.image.load('src/artset/player_vertical.png')
        self._fallen_tile = pygame.image.load('src/artset/player_horizontal.png')
        self._number_moves = 0

    
    def getMoves(self):
        return self._block_state.child_block_states(self._maze)

    def process_move(self, move, arrow):
        prev_block_state = self._block_state
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
        
        if self._block_state != prev_block_state:
            self._number_moves += 1

    def display(self, tile_width, tile_height):
        if self._block_state.fallen:
            scaled_image = pygame.transform.scale(self._fallen_tile, (tile_width,tile_height))
            if(self._block_state.orientation == "horizontal"):
                self._display_surf.blit(scaled_image, ((self._block_state.x-0.5) * tile_width, self._block_state.y * tile_height))
                self._display_surf.blit(scaled_image, ((self._block_state.x+0.5) * tile_width, self._block_state.y * tile_height))
            if(self._block_state.orientation == "vertical"):
                self._display_surf.blit(scaled_image, (self._block_state.x * tile_width, (self._block_state.y + 0.5) * tile_height))
                self._display_surf.blit(scaled_image, (self._block_state.x * tile_width, (self._block_state.y - 0.5) * tile_height))
        else:
            scaled_image = pygame.transform.scale(self._vertical_tile, (tile_width,tile_height))
            self._display_surf.blit(scaled_image, (self._block_state.x * tile_width, self._block_state.y * tile_height))

    
    def _printChildStates(self):
        print("---Available Moves--- : \n")
        moves = self.getMoves()
        for x in range(len(moves)):
            print (moves[x][0] + ',' + str(moves[x][1]))

    def _printCurrentPosition(self):
        print("---Player position---: \n" + str(self._block_state))
