import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *
from states.menus.gamemenu import Menu
from main import *

class SolverMenu(Menu):
    def __init__(self,display_surf,size, moves = 0):
        self._moves = moves
        super().__init__(display_surf,size)

    def _init_menu(self):
        self._menu = pygame_menu.Menu('Solver Menu', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_ORANGE)
        self._menu.add.button('BFS', self._start_game_bfs)
        self._menu.add.button('DFS', self._start_game_dfs)
        self._menu.add.button('Return to Main Menu', self.return_to_main_menu)

    def return_to_main_menu(self):
        pygame.event.post(pygame.event.Event(events['RETURN_TO_MAIN_MENU']))
        self._menu.disable()
    
    def _start_game_bfs(self):
        pygame.event.post(pygame.event.Event(events['START_GAME_BFS']))
        self._menu.disable()
    
    def _start_game_dfs(self):
        pygame.event.post(pygame.event.Event(events['START_GAME_DFS']))
        self._menu.disable()

    def display(self):
        self._menu.mainloop(self._display_surf,disable_loop=True)