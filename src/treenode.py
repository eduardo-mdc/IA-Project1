# A generic definition of a tree node holding a state of the problem
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.check_depth()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.state == other.state
        else:
            return False

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        self.check_depth()
    
    def check_depth(self):
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def heuristic(self, maze):
        
        return distance

    def __str__(self):
        return str(self.state)
    
    def print_parents(self):
        if self.parent is None:
            print(self.state)
        else:
            self.parent.print_parents()
            print(self.state)
    