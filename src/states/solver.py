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
import time
from writer import *
from states.visualizer import *

class Solver:
    def __init__(self,display_surf,matrix_size,start,goal,type,iterations):
        self._display_surf = display_surf
        self._start = start
        self._goal = goal
        self._type = type
        self._iterations = int(iterations)
        self._matrix_size = matrix_size
        self._maze = generate_matrix(matrix_size, start, goal)
        self._player = Player(self._maze,start,self._display_surf)
        print_matrix(self._maze,matrix_size)

    def solve(self):
        start_time = time.time()
        solution = None
        match self._type:
            case "BFS":
                solution = self.solve_BFS()
            case "DFS":
                solution = self.solve_DFS()
            case "GREEDY":
                solution = self.solve_greedy()
            case "A*":
                solution = self.solve_a_star()
            case "COMPARE":
                solution = self.solve_all()
                if solution:
                    end_time = time.time()
                    self.execution_time = round(end_time - start_time,3)
                    write_to_csv(solution,self._iterations,self._matrix_size)
        end_time = time.time()
        self.execution_time = round(end_time - start_time,3)
        print("Execution time:", self.execution_time, "seconds")
        if(solution):
            print("\n\n\n --- Solution : --- \n\n\n")
            print(solution.print_parents())
            self._solution = solution
            return (solution, self.execution_time)
 
        print("No solution found")
        self._solution = None
        return (None, self.execution_time)

    def solve_BFS(self):
        print("Solving with BFS")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        queue = deque([root])   # initialize the queue to store the nodes
        visited = []

        while queue:
            node = queue.popleft()   # get first element in the queue
            node.check_depth()
            #print("Current Position")
            #print(node.state)
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
            #print("Current Position")
            #print(node.state)
            node.check_depth()
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
                    stack.append(leaf)
        return None
    
    def solve_greedy(self):
        print("Solving with Greedy")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        heap = [] # priority queue where the heuristic is the priority
        heapq.heappush(heap, (root.heuristic(self._goal), root))
        visited = []


        while heap:
            node = heapq.heappop(heap)[1] # get node with lowest heuristic
            #print("Current Position")
            #print(node.state)
            node.check_depth()
            if node.state.check_goal(self._goal):
                return node
            
            if node not in visited:
                # add node to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):
                    # create tree node with the new state
                    leaf = TreeNode(state[1])

                    # link child node to its parent in the tree
                    node.add_child(leaf)

                    # push the child node to the heap
                    heapq.heappush(heap, (leaf.heuristic(self._goal), leaf))

        return None
    
    def solve_a_star(self):
        print("Solving with A*")
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        heap = [] # priority queue where the heuristic is the priority
        heapq.heappush(heap, (root.heuristic(self._goal), root))
        visited = []

        while heap:
            node = heapq.heappop(heap)[1] # get node with lowest heuristic
            #print("Current Position")
            #print(node.state)
            node.check_depth()
            if node.state.check_goal(self._goal):
                return node
            
            if node not in visited:
                # add node to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):
                    # create tree node with the new state
                    leaf = TreeNode(state[1])
                    
                    if leaf not in visited:
                        
                        # calculate heuristic for the child node
                        h = leaf.heuristic(self._goal)

                        # calculate estimated total cost to reach goal through current child node
                        f = leaf.depth + h

                        # link child node to its parent in the tree
                        node.add_child(leaf)

                        # Apush child node with its estimated total cost
                        heapq.heappush(heap, (f, leaf))

        return None
    
    def depth_limited_search(self, root, depth_limit):
        stack = [root]   # initialize the stack to store the nodes
        visited = []


        while stack:
            node = stack.pop()   # get last inserted element in the queue
            node.check_depth()
            if node.state.check_goal(self._goal):
                return node

            if node not in visited and node.depth < depth_limit:
                # add leaf to visited
                visited.append(node)
                for state in node.state.child_block_states(self._maze):   # go through next states
                    # create tree node with the new state
                    leaf = TreeNode(state)
                    # link child node to its parent in the tree
                    node.add_child(leaf)
                    # enqueue the child node
                    stack.append(leaf)

        return None

    def solve_iterative_deepening_search(self):
        print("Solving with Iterative Deepening Search")
        #depth_limit = 0
        root = TreeNode(self._player._block_state)   # create the root node in the search tree
        depth_limit = root.depth + 1
        print("depth: ")
        print(depth_limit)

        for depth in range(depth_limit):
            solution = self.depth_limited_search(root, depth)
            if solution:
                return solution

        return None

        while True:
            goal = self.depth_limited_search(depth_limit)
            if goal != None:
                if goal.state.check_goal(self._goal):
                    return goal
            depth_limit += 1

        return None
    
    def _append_solution(self, type):
        start_time = time.time()
        solution = None
        if type == "BFS":
            solution = self.solve_BFS()
        elif type == "DFS":
            solution = self.solve_DFS()
        elif type == "GREEDY":
            solution = self.solve_greedy()
        elif type == "A*":
            solution = self.solve_a_star()
        elif type == "IDS":
            solution = self.solve_a_star()
        execution_time = round(time.time() - start_time,3)

        if solution:
            return (solution.depth, execution_time)
    
        return (None, execution_time)

    def solve_all(self):
        print("Solving with all algorithms")
        bfs = ["bfs"]
        dfs = ["dfs"]
        greedy = ["greedy"]
        a_star = ["a_star"]
        ids = ["ids"]
        for i in range(self._iterations):
            self._regenerate_maze()
            print ("-- Iteration", str(i+1), "of", str(self._iterations) + " -- ")
            print_matrix(self._maze,self._matrix_size)
            bfs.append(self._append_solution("BFS"))
            dfs.append(self._append_solution("DFS"))
            greedy.append(self._append_solution("GREEDY"))
            a_star.append(self._append_solution("A*"))
            ids.append(self._append_solution("IDS"))
        return (bfs, dfs, greedy, a_star, ids)
    
    def _regenerate_maze(self):
        self._maze = generate_matrix(self._matrix_size, self._start, self._goal)
        self._player = Player(self._maze,self._start,self._display_surf)

    