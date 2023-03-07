import pygame
from pygame.locals import *
from states.menu import *
from states.runner import *


class GameHandler:
    def __init__(self, display_surf, size):
        self.state = 'menu'
        self.menu = Menu(display_surf, size)
        self.runner = Runner(display_surf, size)


        