import pygame
from pygame.locals import *
from states.gamestate import *
from states.player import *
from main import * 
from copy import deepcopy
from collections import deque
from treenode import *
from generator import *
import heapq

class Solver:
    def __init__(self,display_surf,matrix_size,start,goal,type):
        self._display_surf = display_surf
        self._goal = goal
        self._type = type
        dead_end_prob = 0.2
        self._maze = generate_matrix(matrix_size, start, goal, dead_end_prob)
        self._player = Player(self._maze,start,self._display_surf)
        print_matrix(self._maze,matrix_size)

    def solve(self):
        solution = None
        #moves = self._player.getMoves()
        match self._type:
            case "BFS":
                solution = self.solve_BFS()
            case "DFS":
                solution = self.solve_DFS()
            case "Greedy":
                solution = self.solve_greedy()
        if(solution):
            print("\n\n\n --- Solution : --- \n\n\n")
            print(solution.print_parents())
            return True
 
        print("No solution found")
        return False



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
            if node.state.check_goal(self._goal):   # check goal state
                return node
            
            if node not in visited:
                # add node to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):   # go through next states
                    # create tree node with the new state
                    leaf = TreeNode(state[1])
            
                    # link child node to its parent in the tree
                    node.add_child(leaf)
                    
                    # enqueue the child node
                    queue.append(leaf)
        return None
    
    def solve_DFS(self):
        print("Solving with DFS")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        stack = [root]   # initialize the stack to store the nodes
        visited = []

        while stack:
            node = stack.pop()   # get last inserted element in the stack
            node.check_depth()
            #print("Current Position")
            #print(node.state)
            if node.state.check_goal(self._maze):   # check goal state
                return node
            
            if node not in visited:
                # add node to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):   # go through next states
                    # create tree node with the new state
                    leaf = TreeNode(state[1])
                    
                    # link child node to its parent in the tree
                    node.add_child(leaf)
                    
                    # enqueue the child node
                    stack.append(leaf)
        return None
    
    def solve_greedy(self):
        print("Solving with Greedy")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        heap = [(root.heuristic(self._goal, self._maze), root)] # priority queue where the heuristic is the priority

        while heap:
            _, node = heapq.heappop(heap) # get node with lowest heuristic

            if node.state.check_goal(self._maze):
                return node
            
            for state in node.state.child_block_states(self._maze):
                # create tree node with the new state
                leaf = TreeNode(state[1])

                # link child node to its parent in the tree
                node.add_child(leaf)

                # push the child node to the heap
                heapq.heappush(heap, (leaf.heuristic(self._maze), leaf))

        return None
    
    def solve_a_star(self):
        print("Solving with A*")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        heap = [(root.heuristic(self._goal, self._maze), root)] # priority queue where the heuristic is the priority

        while heap:
            _, node = heapq.heappop(heap) # get node with lowest heuristic

            if node.state.check_goal(self._maze):
                return node
            
            for state in node.state.child_block_states(self._maze):
                # create tree node with the new state
                leaf = TreeNode(state[1])

                # link child node to its parent in the tree
                node.add_child(leaf)

                # push the child node to the heap
                heapq.heappush(heap, (leaf.heuristic(self._maze), leaf))

        return None