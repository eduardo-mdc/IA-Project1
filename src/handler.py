import pygame
from pygame.locals import *
from states.menus.mainmenu import MainMenu
from states.runner import *


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self.menu = MainMenu(display_surf, size)
        self.runner = Runner(display_surf, size)


        