import pygame
from pygame.locals import *
from states.menus.mainmenu import MainMenu
from states.menus.endingmenu import EndingMenu
from states.menus.solvermenu import SolverMenu
from states.menus.running_algorithm_menu import RunningAlgorithmMenu
from states.menus.ending_algorithm_menu import EndingAlgorithmMenu
from states.menus.compare_algorithms_menu import EndingCompareMenu
import time

from states.runner import *

import json


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self._init_config("config.json")
        self._display_surf = display_surf
        self.size = size
        self.create_menu()


    def printMoves(self):
        print(self.runner.player.getMoves())

    def _init_config(self,config_path):
        with open(config_path) as file:
            self._config = json.load(file)
        self._start = (self._config['game']['start']['x'],self._config['game']['start']['y'])
        self._end = (self._config['game']['end']['x'],self._config['game']['end']['y'])
        self._matrix_size = self._config['game']['matrix_size']
        self._iterations = self._config['solver']['iterations']
        self._wait_time = self._config['solver']['wait_time']

        
    def runner_loop(self):
        self.runner.process_input()
        if(self.runner.player._block_state.check_goal(self._end)):
            pygame.event.post(pygame.event.Event(events['CHANGE_TO_ENDING_MENU']))
    
    def visualizer_loop(self):
        self.visualizer.process_input()
        if(self.visualizer.player._block_state.check_goal(self._end)):
            pygame.event.post(pygame.event.Event(events['RETURN_TO_MAIN_MENU']))
        time.sleep(self._wait_time)
        
    
    def create_runner(self):
        self.runner = Runner(self._display_surf,self.size,self._start,self._end,self._matrix_size)

    def create_visualizer(self,maze,solution):
        self.visualizer = Visualizer(self._display_surf,self.size,self._start,self._end,self._matrix_size,maze,solution)

    def create_solver(self,type):
        self.solver = Solver(self._display_surf,self._matrix_size,self._start,self._end,type,self._iterations)

    def create_ending_menu(self,moves):
        self.ending_menu = EndingMenu(self._display_surf,self.size,moves)

    def create_solver_menu(self):
        self.solver_menu = SolverMenu(self._display_surf,self.size)

    def create_running_algorithm_menu(self):
        self.running_algorithm_menu = RunningAlgorithmMenu(self._display_surf,self.size)

    def create_ending_algorithm_menu(self,ending_type):
        self.ending_algorithm_menu = EndingAlgorithmMenu(self._display_surf,self.size,ending_type)

    def create_compare_algorithms_menu(self,ending_type):
        self.ending_compare_menu = EndingCompareMenu(self._display_surf,self.size,ending_type)
    
    def create_menu(self):
        self.menu = MainMenu(self._display_surf,self.size)
        


        
        
