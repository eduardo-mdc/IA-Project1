import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *
from states.menus.gamemenu import Menu
from main import *

class RunningAlgorithmMenu(Menu):
    def __init__(self,display_surf,size, moves = 0):
        self._moves = moves
        super().__init__(display_surf,size)

    def _init_menu(self):
        self._menu = pygame_menu.Menu('Victory Menu', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_ORANGE)
        self._menu.add.label('Running Algorithm...', "victory_label")

    def display(self):
        self._menu.mainloop(self._display_surf,disable_loop=True)