import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *

class Menu(GameState):
    def __init__(self,display_surf,size):
        super().__init__(display_surf,size)
        self._init_menu()

    def _init_menu(self):
        self._menu = pygame_menu.Menu('AI Block Game', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_GREEN)
        self._menu.add.text_input('Name :', default='John Doe')
        self._menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self._set_difficulty)
        self._menu.add.button('Play', self._start_the_game)
        self._menu.add.button('Quit', pygame_menu.events.EXIT)

    def _set_difficulty(self,value,difficulty):
        print(value)

    def _start_the_game(self):
        print("Started")

    def display(self):
        self._menu.mainloop(self._display_surf)
                
            

