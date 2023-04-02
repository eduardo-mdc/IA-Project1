import pygame
from pygame.locals import *
from handler import *
from states import *
from states.solver import *


events = {
    "START_GAME" : pygame.USEREVENT + 1,
    "CHANGE_TO_SOLVER_MENU" : pygame.USEREVENT + 2,
    "RETURN_TO_MAIN_MENU" : pygame.USEREVENT + 3,
    "CHANGE_TO_ENDING_MENU" : pygame.USEREVENT + 4,
    "RESTART_GAME" : pygame.USEREVENT + 5,
    "START_GAME_BFS" : pygame.USEREVENT + 6,
    "START_GAME_DFS" : pygame.USEREVENT + 7,
    "START_GAME_GREEDY" : pygame.USEREVENT + 8,
    "START_GAME_A_STAR" : pygame.USEREVENT + 9,
    "ENDING_AI_MENU_FAILURE" : pygame.USEREVENT + 10,
    "ENDING_AI_MENU_SUCCESS" : pygame.USEREVENT + 11
}

colors = {
    "BLACK" : (0,0,0),
    "LAVENDER" : (230,230,250),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'WHITE': (255, 255, 255) 
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
    
    def algorithm_event(self, type):
        self._handler.create_running_algorithm_menu()
        self._handler.running_algorithm_menu.display()
        self._handler.create_solver(type)
        self._handler.state = 'ending_solver_menu'
        self._handler.create_ending_algorithm_menu(self._handler.solver.solve())



    #proceeds events like pressed keys, mouse motion etc
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == events['START_GAME']:
            self._handler.create_runner()
            self._handler.state = 'running'
        elif event.type == events['CHANGE_TO_SOLVER_MENU']:
            self._handler.create_solver_menu()
            self._handler.state = 'solver_menu'
        elif event.type == events['RETURN_TO_MAIN_MENU']:
            self._handler.create_menu()
            self._handler.state = 'menu'
        elif event.type == events['CHANGE_TO_ENDING_MENU']:
            self._handler.create_ending_menu(self._handler.runner.player._number_moves)
            self._handler.state = 'ending_menu'
        elif event.type == events['RESTART_GAME']:
            self._handler.create_runner()            
            self._handler.state = 'running'
        elif event.type == events['START_GAME_BFS']:
            self.algorithm_event("BFS")
        elif event.type == events['START_GAME_DFS']:
            self.algorithm_event("DFS")
        elif event.type == events['START_GAME_GREEDY']:
            self.algorithm_event("GREEDY")
        elif event.type == events['START_GAME_A_STAR']:
            self.algorithm_event("A*")
        elif event.type == events['ENDING_AI_MENU_FAILURE']:
            self._handler.create_ending_algorithm_menu("success")
            self._handler.state = 'ending_solver_menu'
            print ("failure")
        elif event.type == events['ENDING_AI_MENU_SUCCESS']:
            self._handler.create_ending_algorithm_menu("failure")
            self._handler.state = 'ending_solver_menu'
            print ("success")


        
        #Parse User Input
        if self._handler.state == 'running':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self._handler.runner.add_input("left")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self._handler.runner.add_input("right")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self._handler.runner.add_input("up")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self._handler.runner.add_input("down")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                pygame.event.post(pygame.event.Event(events['RESTART_GAME']))



    #compute changes in the game world
    def on_loop(self):
        match self._handler.state:
            case 'running':
                self._handler.runner_loop()

    #prints out screen graphics
    def on_render(self):
        match self._handler.state:
            case 'menu':
                self._handler.menu.display()
            case 'running':
                self._handler.runner.display()
            case 'ending_menu':
                self._handler.ending_menu.display()
            case 'solver_menu':
                self._handler.solver_menu.display()
            case 'ending_solver_menu':
                self._handler.ending_algorithm_menu.display()

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