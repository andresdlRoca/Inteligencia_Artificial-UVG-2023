import numpy as np
from queue import Queue

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.solved = False #Sets maze as not solved at the beginning

    def solve(self):
        pass

    def isFree(self, value):
        if value == (255,255,255):
            return True
        
    def getFrontiers(n):
        x,y = n
        return[(x-1, y), (x,y-1),(x+1,y),(x,y+1)]

    def showSolution(self):
        if not self.solved:
            print("Que miras bobo, todavia no esta lista la solucion")
        else:
            # Maze will be displayed here via print and saving an image to the directory
            pass

class BreadthFirstSolver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)
    
    def solve(self, start, end, image):
        #Here we solve the maze via Breadth First Algorithm
        pass
    
    def take_step(self, maze, matrix, step):
        pass
        
class DepthFirstSolver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self):
        pass #Here we solve the maze via Depth First Algorithm

#Possible heuristic functions for A* algorithms:
# 1. Euclidian distance
# 2. Manhattan distance
# 3. Great Circle distance

class A1Solver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self):
        pass #Here we solve the maze via A* algorithm

class A2Solver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self):
        pass #Here we solve the maze via A* algorithm

    