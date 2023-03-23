import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *
from states.menus.gamemenu import Menu
from main import *

class MainMenu(Menu):
    def __init__(self,display_surf,size):
        super().__init__(display_surf,size)

    def _init_menu(self):
        self._menu = pygame_menu.Menu('AI Block Game', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_GREEN)
        self._menu.add.button('Play', self._start_game)
        self._menu.add.button('Play with AI', self._start_game_ai)
        self._menu.add.button('Quit', pygame_menu.events.EXIT)


    def _start_game(self):
        pygame.event.post(pygame.event.Event(events['START_GAME']))
        self._menu.disable()

    def _start_game_ai(self):
        pygame.event.post(pygame.event.Event(events['START_GAME_AI']))
        self._menu.disable()

    def display(self):
        self._menu.mainloop(self._display_surf,disable_loop=True)
                
            

