import pygame
from pygame.locals import *
from states.gamestate import *
from states.player import *
from main import * 
from copy import deepcopy
from collections import deque
from treenode import *

class Solver:
    def __init__(self,maze,player):
        self._maze = maze
        self._player = player

    def solve(self):
        moves = self._player.getMoves()
        self.solve_BFS()

    def solve_BFS(self):
        print("Solving with BFS")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        queue = deque([root])   # initialize the queue to store the nodes
        visited = []

        while queue:
            node = queue.popleft()   # get first element in the queue
            node.check_depth()
            print("Current Position")
            print(node.state)
            if node.state.check_goal(self._maze):   # check goal state
                return node
            
            if node not in visited:
                #add node to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):   # go through next states
                    # create tree node with the new state
                    leaf = TreeNode(state[1])
                    
                    # link child node to its parent in the tree
                    node.add_child(leaf)
                    
                    # enqueue the child node
                    queue.append(leaf)
        return None
    
