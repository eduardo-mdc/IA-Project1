import pygame
from pygame.locals import *
from states.menus.mainmenu import MainMenu
from states.runner import *
import json


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self._init_config("config.json")

        #Game states
        self.menu = MainMenu(display_surf, size)
        self.runner = Runner(display_surf,size,self._start,self._end,self._matrix_size)
        self.solver = Solver(self.runner.maze,self.runner.player,self._end)


    def printMoves(self):
        print(self.runner.player.getMoves())

    def _init_config(self,config_path):
        with open(config_path) as file:
            self._config = json.load(file)
        self._start = (self._config['game']['start']['x'],self._config['game']['start']['y'])
        self._end = (self._config['game']['end']['x'],self._config['game']['end']['y'])
        self._matrix_size = self._config['game']['matrix_size']
        
    def runner_loop(self):
        self.runner.process_input()
        self.runner.check_win(self._end)


        
        