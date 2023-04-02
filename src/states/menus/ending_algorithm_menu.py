import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *
from states.menus.gamemenu import Menu
from main import *

class EndingAlgorithmMenu(Menu):
    def __init__(self,display_surf,size, ending_type):
        self._ending_type = ending_type
        super().__init__(display_surf,size)

    def _init_menu(self):
        self._menu = pygame_menu.Menu('Ending Menu', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_ORANGE)
        if self._ending_type:
            self._menu.add.label('Success!', "success_label")
        else:
            self._menu.add.label('Failure!', "fail_label")

        self._menu.add.button('Return to Main Menu', self.return_to_main_menu)
    
    def return_to_main_menu(self):
        pygame.event.post(pygame.event.Event(events['RETURN_TO_MAIN_MENU']))
        self._menu.disable()

    def display(self):
        self._menu.mainloop(self._display_surf,disable_loop=True)