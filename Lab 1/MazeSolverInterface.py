import numpy as np

class MazeSolver:
    def __init__(self, image):
        self.image = image #Matrix/Image already discretized
        self.solved = False #Sets maze as not solved at the beginning
        self.solvedImage = []

    def solve(self):
        pass
    
    def showSolution(self):
        if not self.solved:
            print("La solucion no esta lista")
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
        print(i[0], j[0])
        solutionMatrix[i[0]][j[0]] = 1
        step = 0
        solvedMatrix = self.take_step(self.image, solutionMatrix, step, end)
        i, j = end[0][0], end[1][0]
        step = solvedMatrix[i][j]
        path = [(i,j)]

        #Generates a path according to the BFS algorithm results, returns coordinates to draw over the original discretized image/array
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
        resultMatrix = self.draw_matrix(self.image, path)
        self.solved = True
        return resultMatrix
    
    #BFS Algorithm
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
    
    #Draws over discretized image according to the path found by the algorithm
    def draw_matrix(self, image, solutionPath):
        path_color = (159,59,212)
        solutionPath = solutionPath[1:-1]
        for x in solutionPath:
            image[x[0]][x[1]] = path_color
        return image

        
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

    