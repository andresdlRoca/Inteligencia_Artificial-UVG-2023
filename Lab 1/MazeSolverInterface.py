import numpy as np

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
    
    def coordinateFinder(self, color):
        im = np.array(self.maze)
        X, Y = np.where(np.all(im==color, axis=2))
        zippedCords = np.column_stack((X,Y))
        return(zippedCords)

class DepthFirstSolver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self):
        pass #Here we solve the maze via Depth First Algorithm

class BreadthFirstSolver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self, start, end):
        #pass #Here we solve the maze via Breadth First Algorithm
        solutionMatrix = []
        for x in range(len(self.maze)):
            solutionMatrix.append([])
            for y in range(len(self.maze[x])):
                solutionMatrix[-1].append(0)
        x, y = start
        solutionMatrix[x][y] = 1
        step = 0
        while solutionMatrix[end[0]][end[1]] == 0:
            step +=1
            self.take_step(self.maze, solutionMatrix, step)
        x,y = end
        step = solutionMatrix[x][y]
        shortestPath = [(x,y)]
        while step > 1:
            if x > 0 and solutionMatrix[x-1][y] == step-1:
                x, y = x-1, y
                shortestPath.append((x,y))
    
    def take_step(maze, matrix, step):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == step:
                    if x>0 and matrix[x-1][y] == 0 and maze[x-1][y] == 0:
                        matrix[x-1][y] = step + 1
                    if y>0 and matrix[x][y-1] == 0 and maze[x][y-1] == 0:
                        matrix[x][y-1] = step+1
                    if x<len(matrix)-1 and matrix[x+1][y] == 0 and maze[x+1][y] == 0:
                        matrix[x+1][y]=step+1
                    if y<len(matrix[1])-1 and matrix[x][y+1] == 0 and maze[x][y+1] == 0:
                        matrix[x][y+1] = step+1
        

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

    