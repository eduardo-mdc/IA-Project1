import pygame
from pygame.locals import *
from states.gamestate import *
from states.player import *
from main import * 
import random

class Solver():
    def __init__(self,maze,player):
        self._maze = maze
        self._player = player

    def solve(self):
        moves = self._player.getMoves()
        print("SOLVING")
    

