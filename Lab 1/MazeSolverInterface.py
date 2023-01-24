import numpy as np
from queue import Queue
from PIL import Image, ImageDraw

class MazeSolver:
    def __init__(self, image):
        self.image = image #Matrix/Image already discretized
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

    def solve(self, start, end):
        #Here we solve the maze via Breadth First Algorithm
        solutionMatrix = np.zeros(np.shape(self.image))
        i,j = start
        solutionMatrix[i[0]][j[0]] = 1
        step = 0
        solvedMatrix = self.take_step(self.image, solutionMatrix, step, end)
        # print(solvedMatrix)
        # self.solved = True
        i, j = end[0][0], end[1][0]
        step = solvedMatrix[i][j]
        path = [(i,j)]
        while step[0] > 1:
            if i > 0 and step-1 in solvedMatrix[i-1][j]:
                i, j = i-1, j
                path.append((i,j))
                step-=1
            elif j> 0 and step-1 in solvedMatrix[i][j-1]:
                i,j=i,j-1
                path.append((i,j))
                step -= 1
            elif i<len(solvedMatrix) - 1 and step-1 in solvedMatrix[i+1][j]:
                i,j = i+1, j
                path.append((i,j))
                step -= 1
            elif j<len(solvedMatrix[i]) - 1 and step - 1 in solvedMatrix[i][j+1]:
                i,j = i, j+1
                path.append((i,j))
                step -= 1
            

            # self.draw_matrix(self.image, solvedMatrix)
        resultMatrix = self.draw_matrix(self.image, path)
        return resultMatrix
    
    def take_step(self, image, matrix, step, end):
        while [0,0,0] in matrix[end[0][0]][end[1][0]]:
            step += 1
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    if step in matrix[x][y]:
                        if x>0 and (0,0,0) in matrix[x-1][y] and (255,255,255) in image[x-1][y]:
                            matrix[x-1][y] = step + 1
                        if y>0 and (0,0,0) in matrix[x][y-1] and (255,255,255) in image[x][y-1]:
                            matrix[x][y-1] = step + 1
                        if x<len(matrix)-1 and (0,0,0) in matrix[x+1][y] and (255,255,255) in image[x+1][y]:
                            matrix[x+1][y] = step + 1
                        if y<len(matrix[x])-1 and (0,0,0) in matrix[x][y+1] and (255,255,255) in image[x][y+1]:
                            matrix[x][y+1] = step+1
        return matrix
    
    def draw_matrix(self, image, solutionPath):
        path_color = (159,59,212)
        solutionPath = solutionPath[1:-1]
        for x in solutionPath:
            image[x[0]][x[1]] = path_color
        return image


    def showSolution(self):
        if self.solved:
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

    