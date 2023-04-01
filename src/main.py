import pygame
from pygame.locals import *
from handler import *
from states import *
from states.solver import *


events = {
    "START_GAME" : pygame.USEREVENT + 1,
    "START_GAME_AI" : pygame.USEREVENT + 2,
    "RETURN_TO_MAIN_MENU" : pygame.USEREVENT + 3
}

colors = {
    "BLACK" : (0,0,0),
    "LAVENDER" : (230,230,250),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'WHITE': (255, 255, 255)  # Add this line
}

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._screenSize = [800,800]
        self.size = self.weight, self.height = self._screenSize[0], self._screenSize[1]
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._handler = GameHandler(self._display_surf, self.size)
 
    #proceeds events like pressed keys, mouse motion etc
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == events['START_GAME']:
            self._handler.state = 'running'
        elif event.type == events['START_GAME_AI']:
            self._handler.state = 'running_ai'
            #TEMPORARY
            solution = self._handler.solver.solve()
            if(solution):
                print("Solution :")
                print(solution.print_parents())
            else:
                print("No solution found")
        elif event.type == events['RETURN_TO_MAIN_MENU']:
            self._handler.state = 'menu'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self._handler.runner.add_input("left")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self._handler.runner.add_input("right")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self._handler.runner.add_input("up")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self._handler.runner.add_input("down")


    #compute changes in the game world
    def on_loop(self):
        match self._handler.state:
            case 'menu':
                pass
            case 'running':
                self._handler.runner_loop()
            case 'running_ai':
                pass
            case 'ending_menu':
                pass

    #prints out screen graphics
    def on_render(self):
        match self._handler.state:
            case 'menu':
                self._handler.menu.display()
            case 'running':
                self._handler.runner.display()
            case 'running_ai':
                pass
            case 'ending_menu':
                self._handler.ending_menu.display()

        pygame.display.flip()


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