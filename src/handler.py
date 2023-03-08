import pygame
from pygame.locals import *
from states.menus.mainmenu import MainMenu
from states.runner import *
import json


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self._getConfiguration("config.json")
        self.menu = MainMenu(display_surf, size)
        self.runner = Runner(display_surf, size,self._config)

    def _getConfiguration(self,config_path):
        with open(config_path) as file:
            self._config = json.load(file)

        
        