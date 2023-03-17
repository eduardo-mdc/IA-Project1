class BlockState:
    def __init__(self,x = 0,y = 0,fallen = False,orientation = None):
        self.x = x
        self.y = y
        self.fallen = fallen
        self.orientation = orientation

    def display(self):
        print("WARNING : Call to display() on <Block> Class")

    def fall_r(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x+1][state.y] == 1 and maze[state.x+2][state.y] == 1) or
        (maze[state.x+1][state.y] == 1 and maze[state.x+2][state.y] == 2) or
        (maze[state.x+1][state.y] == 2 and maze[state.x+2][state.y] == 1))):
            return BlockState(state.x+1.5, state.y,True, "horizontal")
        
    def fall_l(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x-1][state.y] == 1 and maze[state.x-2][state.y] == 1) or
        (maze[state.x-1][state.y] == 1 and maze[state.x-2][state.y] == 2) or
        (maze[state.x-1][state.y] == 2 and maze[state.x-2][state.y] == 1))):
            return BlockState(state.x-1.5, state.y,True, "horizontal")
        
    def fall_u(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x][state.y-1] == 1 and maze[state.x][state.y-2] == 1) or
        (maze[state.x][state.y-1] == 1 and maze[state.x][state.y-2] == 2) or
        (maze[state.x][state.y-1] == 2 and maze[state.x][state.y-2] == 1))):
            return BlockState(state.x, state.y-1.5,True, "horizontal")
        
    def fall_d(state, maze):
        if (state.fallen == False and state.orientation == None and
        ((maze[state.x][state.y+1] == 1 and maze[state.x][state.y+2] == 1) or
        (maze[state.x][state.y+1] == 1 and maze[state.x][state.y+2] == 2) or
        (maze[state.x][state.y+1] == 2 and maze[state.x][state.y+2] == 1))):
            return BlockState(state.x, state.y+1.5,True, "horizontal")
        
    # orientation guardada como string? nao gostei
    def get_up_r(state, maze):
        if(state.fallen == True and state.orientation == "horizontal" and maze[state.x+1.5][state.y] == 1):
            return BlockState(state.x+1.5, state.y,False, None)
        
    def get_up_l(state, maze):
        if(state.fallen == True and state.orientation == "horizontal" and maze[state.x-1.5][state.y] == 1):
            return BlockState(state.x-1.5, state.y,False, None)
        
    def get_up_u(state, maze):
        if(state.fallen == True and state.orientation == "vertical" and maze[state.x][state.y-1.5] == 1):
            return BlockState(state.x, state.y-1.5,False, None)

    def get_up_d(state, maze):
        if(state.fallen == True and state.orientation == "vertical" and maze[state.x][state.y+1.5] == 1):
            return BlockState(state.x, state.y+1.5,False, None)
        
    def roll_r(state, maze):
        if (state.fallen == True and state.orientation == "vertical" and
        ((maze[state.x+1][state.y-0.5] == 1 and maze[state.x+1][state.y+0.5] == 1) and
        (maze[state.x+1][state.y-0.5] == 1 and maze[state.x+1][state.y+0.5] == 2) and
        (maze[state.x+1][state.y-0.5] == 2 and maze[state.x+1][state.y+0.5] == 1))):
            return BlockState(state.x+1, state.y,True, "horizontal")
        
    def roll_l(state, maze):
        if (state.fallen == True and state.orientation == "vertical" and
        ((maze[state.x-1][state.y-0.5] == 1 and maze[state.x-1][state.y+0.5] == 1) and
        (maze[state.x-1][state.y-0.5] == 1 and maze[state.x-1][state.y+0.5] == 2) and
        (maze[state.x-1][state.y-0.5] == 2 and maze[state.x-1][state.y+0.5] == 1))):
            return BlockState(state.x-1, state.y,True, "horizontal")
        
    def roll_u(state, maze):
        if (state.fallen == True and state.orientation == "horizontal" and
        ((maze[state.x-0.5][y-1] == 1 and maze[state.x+0.5][state.y-1] == 1) and
        (maze[state.x-0.5][state.y-1] == 1 and maze[state.x+0.5][state.y-1] == 2) and
        (maze[state.x-0.5][state.y-1] == 2 and maze[state.x+0.5][state.y-1] == 1))):
            return BlockState(state.x, state.y-1,True, "horizontal")
        
    def roll_d(state, maze):
        if (state.fallen == True and state.orientation == "horizontal" and
        ((maze[state.x-0.5][state.y+1] == 1 and maze[state.x+0.5] [state.y+1] == 1) and
        (maze[state.x-0.5][state.y+1] == 1 and maze[state.x+0.5][state.y+1] == 2) and
        (maze[state.x-0.5][state.y+1] == 2 and maze[state.x+0.5][state.y+1] == 1))):
            return BlockState(state.x+1, state.y+1,True, "horizontal")
        
    def child_block_states(state, maze):
        new_states = []
        if(BlockState.fall_r(state, maze)):
            new_states.append(["fall_r",BlockState.fall_r(state, maze)])
        if(BlockState.fall_l(state, maze)):
            new_states.append(["fall_l",BlockState.fall_l(state, maze)])
        if(BlockState.fall_d(state, maze)):
            new_states.append(["fall_d",BlockState.fall_d(state, maze)])
        if(BlockState.fall_u(state, maze)):
            new_states.append(["fall_u",BlockState.fall_u(state, maze)])
        if(BlockState.get_up_r(state, maze)):
            new_states.append(["get_up_r",BlockState.get_up_r(state, maze)])
        if(BlockState.get_up_l(state, maze)):
            new_states.append(["get_up_l",BlockState.get_up_l(state, maze)])
        if(BlockState.get_up_d(state, maze)):
            new_states.append(["get_up_d",BlockState.get_up_d(state, maze)])
        if(BlockState.get_up_u(state, maze)):
            new_states.append(["get_up_u",BlockState.get_up_u(state, maze)])
        if(BlockState.roll_r(state, maze)):
            new_states.append(["roll_r",BlockState.roll_r(state, maze)])
        if(BlockState.roll_l(state, maze)):
            new_states.append(["roll_l",BlockState.roll_l(state, maze)])
        if(BlockState.roll_d(state, maze)):
            new_states.append(["roll_d",BlockState.roll_d(state, maze)])
        if(BlockState.roll_u(state, maze)):
            new_states.append(["roll_u",BlockState.roll_u(state, maze)])
        return new_states
    
    def check_hole(new_state, maze):
        if(new_state.orientation == None):
                if(maze[new_state.x][new_state.y-1] == 2):
                    return True
        return False
    
    def check_goal(new_state, maze):
        if(new_state.orientation == None):
                if(maze[new_state.x][new_state.y-1] == 9):
                    return True
        return False
    
    def __str__(self):
        output = 'BlockState <'+ str(id(self)) +'>\n'
        output += '     X           : '+ str(self.x) +'\n'
        output += '     Y           : '+ str(self.y) +'\n'
        output += '     Fallen      : '+ str(self.fallen) +'\n'
        output += '     Orientation : '+ str(self.orientation) +'\n'
        return output