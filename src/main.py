import pygame
from pygame.locals import *
from handler import *
from states import *


events = {
    "START_GAME" : pygame.USEREVENT + 1
}

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._screenSize = [800,600]
        self.size = self.weight, self.height = self._screenSize[0], self._screenSize[1]
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._handler = GameHandler(self._display_surf, self.size)
 
    #proceeds events like pressed keys, mouse motion etc
    def on_event(self, event):
        print(str(event))
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == events['START_GAME']:
            self._handler.state = 'running'

    #compute changes in the game world
    def on_loop(self):
        match self._handler.state:
            case 'menu':
                pass
            case 'running':
                pass


    #prints out screen graphics
    def on_render(self):
        match self._handler.state:
            case 'menu':
                self._handler.menu.display()
            case 'running':
                self._handler.runner.display()

    #removes remaining objects.
    def on_cleanup(self):
        pygame.quit()
        exit()
 
    #initializes game, and holds main loop
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


def main(): 
    if __name__ == "__main__":
        application = App()
        application.on_execute()


main()