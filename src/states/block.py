class BlockState:
    def __init__(self,x = 0,y = 0,fallen = False,orientation = None):
        self.x = x
        self.y = y
        self.fallen = fallen
        self.orientation = orientation

    def display(self):
        print("WARNING : Call to display() on <Block> Class")

    def fall_r(self, maze):
        if (self.fallen == False and self.orientation == None and
        ((maze[self.x+1][self.y] == 1 and maze[self.x+2][self.y] == 1) or
        (maze[self.x+1][self.y] == 1 and maze[self.x+2][self.y] == 2) or
        (maze[self.x+1][self.y] == 2 and maze[self.x+2][self.y] == 1))):
            return BlockState(self.x+1.5, self.y,True, "horizontal")
        
    def fall_l(self, maze):
        if (self.fallen == False and self.orientation == None and
        ((maze[self.x-1][self.y] == 1 and maze[self.x-2][self.y] == 1) or
        (maze[self.x-1][self.y] == 1 and maze[self.x-2][self.y] == 2) or
        (maze[self.x-1][self.y] == 2 and maze[self.x-2][self.y] == 1))):
            return BlockState(self.x-1.5, self.y,True, "horizontal")
        
    def fall_u(self, maze):
        if (self.fallen == False and self.orientation == None and
        ((maze[self.x][self.y-1] == 1 and maze[self.x][self.y-2] == 1) or
        (maze[self.x][self.y-1] == 1 and maze[self.x][self.y-2] == 2) or
        (maze[self.x][self.y-1] == 2 and maze[self.x][self.y-2] == 1))):
            return BlockState(self.x, self.y-1.5,True, "horizontal")
        
    def fall_d(self, maze):
        if (self.fallen == False and self.orientation == None and
        ((maze[self.x][self.y+1] == 1 and maze[self.x][self.y+2] == 1) or
        (maze[self.x][self.y+1] == 1 and maze[self.x][self.y+2] == 2) or
        (maze[self.x][self.y+1] == 2 and maze[self.x][self.y+2] == 1))):
            return BlockState(self.x, self.y+1.5,True, "horizontal")
        
    # orientation guardada como string? nao gostei
    def get_up_r(self, maze):
        if(self.fallen == True and self.orientation == "horizontal" and maze[self.x+1.5][self.y] == 1):
            return BlockState(self.x+1.5, self.y,False, None)
        
    def get_up_l(self, maze):
        if(self.fallen == True and self.orientation == "horizontal" and maze[self.x-1.5][self.y] == 1):
            return BlockState(self.x-1.5, self.y,False, None)
        
    def get_up_u(self, maze):
        if(self.fallen == True and self.orientation == "vertical" and maze[self.x][self.y-1.5] == 1):
            return BlockState(self.x, self.y-1.5,False, None)

    def get_up_d(self, maze):
        if(self.fallen == True and self.orientation == "vertical" and maze[self.x][self.y+1.5] == 1):
            return BlockState(self.x, self.y+1.5,False, None)
        
    def roll_r(self, maze):
        if (self.fallen == True and self.orientation == "vertical" and
        ((maze[self.x+1][self.y-0.5] == 1 and maze[self.x+1][self.y+0.5] == 1) and
        (maze[self.x+1][self.y-0.5] == 1 and maze[self.x+1][self.y+0.5] == 2) and
        (maze[self.x+1][self.y-0.5] == 2 and maze[self.x+1][self.y+0.5] == 1))):
            return BlockState(self.x+1, self.y,True, "horizontal")
        
    def roll_l(self, maze):
        if (self.fallen == True and self.orientation == "vertical" and
        ((maze[self.x-1][self.y-0.5] == 1 and maze[self.x-1][self.y+0.5] == 1) and
        (maze[self.x-1][self.y-0.5] == 1 and maze[self.x-1][self.y+0.5] == 2) and
        (maze[self.x-1][self.y-0.5] == 2 and maze[self.x-1][self.y+0.5] == 1))):
            return BlockState(self.x-1, self.y,True, "horizontal")
        
    def roll_u(self, maze):
        if (self.fallen == True and self.orientation == "horizontal" and
        ((maze[self.x-0.5][y-1] == 1 and maze[self.x+0.5][self.y-1] == 1) and
        (maze[self.x-0.5][self.y-1] == 1 and maze[self.x+0.5][self.y-1] == 2) and
        (maze[self.x-0.5][self.y-1] == 2 and maze[self.x+0.5][self.y-1] == 1))):
            return BlockState(self.x, self.y-1,True, "horizontal")
        
    def roll_d(self, maze):
        if (self.fallen == True and self.orientation == "horizontal" and
        ((maze[self.x-0.5][self.y+1] == 1 and maze[self.x+0.5] [self.y+1] == 1) and
        (maze[self.x-0.5][self.y+1] == 1 and maze[self.x+0.5][self.y+1] == 2) and
        (maze[self.x-0.5][self.y+1] == 2 and maze[self.x+0.5][self.y+1] == 1))):
            return BlockState(self.x+1, self.y+1,True, "horizontal")
        
    def child_block_states(self, maze):
        new_states = []
        if(BlockState.fall_r(self, maze)):
            new_states.append(["fall_r",BlockState.fall_r(self, maze)])
        if(BlockState.fall_l(self, maze)):
            new_states.append(["fall_l",BlockState.fall_l(self, maze)])
        if(BlockState.fall_d(self, maze)):
            new_states.append(["fall_d",BlockState.fall_d(self, maze)])
        if(BlockState.fall_u(self, maze)):
            new_states.append(["fall_u",BlockState.fall_u(self, maze)])
        if(BlockState.get_up_r(self, maze)):
            new_states.append(["get_up_r",BlockState.get_up_r(self, maze)])
        if(BlockState.get_up_l(self, maze)):
            new_states.append(["get_up_l",BlockState.get_up_l(self, maze)])
        if(BlockState.get_up_d(self, maze)):
            new_states.append(["get_up_d",BlockState.get_up_d(self, maze)])
        if(BlockState.get_up_u(self, maze)):
            new_states.append(["get_up_u",BlockState.get_up_u(self, maze)])
        if(BlockState.roll_r(self, maze)):
            new_states.append(["roll_r",BlockState.roll_r(self, maze)])
        if(BlockState.roll_l(self, maze)):
            new_states.append(["roll_l",BlockState.roll_l(self, maze)])
        if(BlockState.roll_d(self, maze)):
            new_states.append(["roll_d",BlockState.roll_d(self, maze)])
        if(BlockState.roll_u(self, maze)):
            new_states.append(["roll_u",BlockState.roll_u(self, maze)])
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