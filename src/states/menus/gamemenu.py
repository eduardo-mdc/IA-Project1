import pygame
import pygame_menu
from pygame.locals import *
from states.gamestate import *

class Menu(GameState):
    def __init__(self,display_surf,size):
        super().__init__(display_surf,size)
        self._init_menu()

    def _init_menu(self):
        print("WARNING : Call to _init_menu() on <Menu> Class")

    def display(self):
        print("WARNING : Call to display() on <Menu> Class")
                
            

