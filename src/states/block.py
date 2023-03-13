class BlockState:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.fallen = False
        self.orientation = None

    def __init__(self, x, y, fallen, orientation):
        self.x = x
        self.y = y
        self.fallen = fallen
        self.orientation = orientation

    def display(self):
        print("WARNING : Call to display() on <Block> Class")

    def fall_r(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x+1, state.y][state.y] == 1 and maze[state.x+2, state.y][state.y] == 1) or
        (maze[state.x+1, state.y][state.y] == 1 and maze[state.x+2, state.y][state.y] == 2) or
        (maze[state.x+1, state.y][state.y] == 2 and maze[state.x+2, state.y][state.y] == 1))):
            return BlockState(True, "horizontal", state.x+1.5, state.y)
        
    def fall_l(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x-1, state.y][state.y] == 1 and maze[state.x-2, state.y][state.y] == 1) or
        (maze[state.x-1, state.y][state.y] == 1 and maze[state.x-2, state.y][state.y] == 2) or
        (maze[state.x-1, state.y][state.y] == 2 and maze[state.x-2, state.y][state.y] == 1))):
            return BlockState(True, "horizontal", state.x-1.5, state.y)
        
    def fall_u(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x, state.y-1][state.y] == 1 and maze[state.x, state.y-2][state.y] == 1) or
        (maze[state.x, state.y-1][state.y] == 1 and maze[state.x, state.y-2][state.y] == 2) or
        (maze[state.x, state.y-1][state.y] == 2 and maze[state.x, state.y-2][state.y] == 1))):
            return BlockState(True, "horizontal", state.x, state.y-1.5)
        
    def fall_u(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x, state.y+1][state.y] == 1 and maze[state.x, state.y+2][state.y] == 1) or
        (maze[state.x, state.y+1][state.y] == 1 and maze[state.x, state.y+2][state.y] == 2) or
        (maze[state.x, state.y+1][state.y] == 2 and maze[state.x, state.y+2][state.y] == 1))):
            return BlockState(True, "horizontal", state.x, state.y+1.5)
        
    # orientation guardada como string? nao gostei
    def get_up_r(state, maze):
        if(state.fallen == True and state.orientation == "horizontal" and maze[state.x+1.5][state.y] == 1):
            return BlockState(False, None, state.x+1.5, state.y)
        
    def get_up_l(state, maze):
        if(state.fallen == True and state.orientation == "horizontal" and maze[state.x-1.5][state.y] == 1):
            return BlockState(False, None, state.x-1.5, state.y)
        
    def get_up_u(state, maze):
        if(state.fallen == True and state.orientation == "vertical" and maze[state.x][state.y-1.5] == 1):
            return BlockState(False, None, state.x, state.y-1.5)

    def get_up_d(state, maze):
        if(state.fallen == True and state.orientation == "vertical" and maze[state.x][state.y+1.5] == 1):
            return BlockState(False, None, state.x, state.y+1.5)
        
    def roll_r(state, maze):
        if (state.fallen == True and state.orientation == "vertical" and
        ((maze[state.x+1][state.y-0.5] == 1 and maze[state.x+1][state.y+0.5] == 1) and
        (maze[state.x+1][state.y-0.5] == 1 and maze[state.x+1][state.y+0.5] == 2) and
        (maze[state.x+1][state.y-0.5] == 2 and maze[state.x+1][state.y+0.5] == 1))):
            return BlockState(True, "horizontal", state.x+1, state.y)
        
    def roll_l(state, maze):
        if (state.fallen == True and state.orientation == "vertical" and
        ((maze[state.x-1][state.y-0.5] == 1 and maze[state.x-1][state.y+0.5] == 1) and
        (maze[state.x-1][state.y-0.5] == 1 and maze[state.x-1][state.y+0.5] == 2) and
        (maze[state.x-1][state.y-0.5] == 2 and maze[state.x-1][state.y+0.5] == 1))):
            return BlockState(True, "horizontal", state.x-1, state.y)
        
    def roll_u(state, maze):
        if (state.fallen == True and state.orientation == "horizontal" and
        ((maze[state.x-0.5][y-1] == 1 and maze[state.x+0.5][state.y-1] == 1) and
        (maze[state.x-0.5][state.y-1] == 1 and maze[state.x+0.5][state.y-1] == 2) and
        (maze[state.x-0.5][state.y-1] == 2 and maze[state.x+0.5][state.y-1] == 1))):
            return BlockState(True, "horizontal", state.x, state.y-1)
        
    def roll_d(state, maze):
        if (state.fallen == True and state.orientation == "horizontal" and
        ((maze[state.x-0.5][state.y+1] == 1 and maze[state.x+0.5][state.y+1] == 1) and
        (maze[state.x-0.5][state.y+1] == 1 and maze[state.x+0.5][state.y+1] == 2) and
        (maze[state.x-0.5][state.y+1] == 2 and maze[state.x+0.5][state.y+1] == 1))):
            return BlockState(True, "horizontal", state.x+1, state.y+1)