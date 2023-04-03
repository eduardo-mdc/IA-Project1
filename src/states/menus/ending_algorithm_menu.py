import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *
from states.menus.gamemenu import Menu
from main import *

class EndingAlgorithmMenu(Menu):
    def __init__(self,display_surf,size, solution):
        self._solution = solution
        super().__init__(display_surf,size)

    def _init_menu(self):
        self._menu = pygame_menu.Menu('Ending Menu', self._size[0], self._size[1],theme=pygame_menu.themes.THEME_ORANGE)
        if self._solution[0]:
            self._menu.add.label('Success!', "success_label")
            self._menu.add.label('Number of Moves : ' + str(self._solution[0].depth), "moves_label")
        else:
            self._menu.add.label('Failure!', "fail_label")
        
        self._menu.add.label('Execution Time : ' + str(self._solution[1]) + " seconds", "time_label")


        self._menu.add.button('Return to Main Menu', self.return_to_main_menu)
    
    def return_to_main_menu(self):
        pygame.event.post(pygame.event.Event(events['RETURN_TO_MAIN_MENU']))
        self._menu.disable()

    def display(self):
        self._menu.mainloop(self._display_surf,disable_loop=True)