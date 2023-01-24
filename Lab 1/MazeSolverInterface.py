import numpy as np
from queue import Queue

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.solved = False #Sets maze as not solved at the beginning

    def solve(self):
        pass

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
        solutionMatrix = np.zeros(np.shape(image))
        i,j = start
        print(i, j)
        solutionMatrix[i][j] = 1
        step = 0
        solvedMatrix = self.take_step(image, solutionMatrix, step, end)
        print(solvedMatrix)
    
    def take_step(self, image, matrix, step, end):
        while matrix[end[0][0]][end[1][0]] == 0:
            step += 1
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    if matrix[x][y] == step:
                        if x>0 and matrix[x-1][y] == (0,0,0) and image[x-1][y] == (255,255,255):
                            matrix[x-1][y] = step + 1
                        if y>0 and matrix[x][y-1] == (0,0,0) and image[x][y-1] == (255,255,255):
                            matrix[x][y-1] = step + 1
                        if x<len(matrix)-1 and matrix[x+1][y] == (0,0,0) and image[x+1][y] == (255,255,255):
                            matrix[x+1][y] = step + 1
                        if y<len(matrix[x])-1 and matrix[x][y+1] == (0,0,0) and image[x][y+1] == (255,255,255):
                            matrix[x][y+1] = step+1
        return matrix
        
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

    