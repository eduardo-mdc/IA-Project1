class GameState:
    def __init__(self,display_surf, size):
        self._display_surf = display_surf
        self._size = size

    def display(self):
        print("WARNING : Call to display() on <GameState> Class")
