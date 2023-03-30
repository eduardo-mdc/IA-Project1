import pygame
from pygame.locals import *
from states.menus.mainmenu import MainMenu
from states.menus.endingmenu import EndingMenu
from states.runner import *
import json


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self._init_config("config.json")

        #Game Menu's
        self.menu = MainMenu(display_surf, size)
        self.ending_menu = EndingMenu(display_surf,size)
        #Game states
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
        if(self.runner.player._block_state.check_goal(self._end)):
            self.state = 'ending_menu'
            self.ending_menu._moves = self.runner.player._number_moves
        


        
        