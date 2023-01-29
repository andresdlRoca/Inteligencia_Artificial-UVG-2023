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
        while [0,0,0] in matrix[end[0][0]][end[1][0]] or [0,0,0] in matrix[end[0][0]][end[1][0]]:
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
        self.path = []

    def solve(self, start, end):
        #Here we solve the maze via DFS Algorithm
        solutionMatrix = np.zeros(np.shape(self.image))
        i,j = start
        solutionMatrix[i[0]][j[0]] = 1
        step = 0
        solvedMatrix = self.take_step(i[0], j[0], self.image, solutionMatrix, step, end)
        i, j = end[0][0], end[1][0]
        step = solvedMatrix[i][j]
        path = [(i,j)]
        #Generates a path according to the DFS algorithm results, returns coordinates to draw over the original discretized image/array
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
    
    #DFS Algorithm
    def take_step(self,x,y,image,matrix,step,end):
        step += 1
        if [0,0,0] in matrix[end[0][0]][end[1][0]]:
            if step in matrix[x][y]:
                if x>0 and (0,0,0) in matrix[x-1][y] and (255,255,255) in image[x-1][y]:
                    matrix[x-1][y] = step + 1
                    self.take_step(x-1, y, image,matrix,step,end)
                if y>0 and (0,0,0) in matrix[x][y-1] and (255,255,255) in image[x][y-1]:
                    matrix[x][y-1] = step + 1
                    self.take_step(x, y-1,image,matrix,step,end)
                if x<len(matrix)-1 and (0,0,0) in matrix[x+1][y] and (255,255,255) in image[x+1][y]:
                    matrix[x+1][y] = step + 1
                    self.take_step(x+1, y,image,matrix,step,end)
                if y<len(matrix[x])-1 and (0,0,0) in matrix[x][y+1] and (255,255,255) in image[x][y+1]:
                    matrix[x][y+1] = step+1
                    self.take_step(x, y+1,image,matrix,step,end)
        return matrix

    #Draws over discretized image according to the path found by the algorithm
    def draw_matrix(self, image, solutionPath):
        path_color = (159,59,212)
        solutionPath = solutionPath[1:-1]
        for x in solutionPath:
            image[x[0]][x[1]] = path_color
        return image



class AStarSolver(MazeSolver):
    def __init__(self, maze):
        super().__init__(maze)

    def solve(self, start, end):
        #Here we solve the maze via A* Algorithm
        solutionMatrix = np.zeros(np.shape(self.image))
        i,j = start
        a,b = end
        solutionMatrix[i[0]][j[0]] = 1
        step = 0
        solvedMatrix = self.take_step(i[0], j[0], self.image, solutionMatrix, step, a[0], b[0])
        resultMatrix = self.draw_matrix(self.image, solvedMatrix)
        self.solved = True
        return resultMatrix #Returns shortestPath
    
    def take_step(self, x_start, y_start, image, matrix, step, x_end, y_end):
        heuristic = lambda x,y: abs(x_end - x) + abs(y_end - y) #Manhattan heuristic
        comp = lambda state: state[2] + state[3] #Total cost

        fringe = [((x_start,y_start), list(), 0, heuristic(x_start, y_start))]
        visited = {}

        while True:
            state = fringe.pop(0)

            (x,y)=state[0]

            if [0,0,0] not in matrix[x_end][y_end]:
                path = [state[0]] + state[1]
                path.reverse()
                return path
            
            visited[(x,y)] = state[2]

            neighbor = list()
            if x>0 and (0,0,0) in matrix[x-1][y] and (255,255,255) in image[x-1][y]:
                matrix[x-1][y] = step + 1
                neighbor.append((x-1,y))
            if y>0 and (0,0,0) in matrix[x][y-1] and (255,255,255) in image[x][y-1]:
                matrix[x][y-1] = step + 1
                neighbor.append((x,y-1))
            if x<len(matrix)-1 and (0,0,0) in matrix[x+1][y] and (255,255,255) in image[x+1][y]:
                matrix[x+1][y] = step + 1
                neighbor.append((x+1,y))
            if y<len(matrix[x])-1 and (0,0,0) in matrix[x][y+1] and (255,255,255) in image[x][y+1]:
                matrix[x][y+1] = step+1
                neighbor.append((x,y+1))
            
            for n in neighbor:
                next_cost = state[2] + 1
                if n in visited and visited[n] >= next_cost:
                    continue
                fringe.append((n, [state[0]] + state[1], next_cost, heuristic(n[0], n[1])))
            
            fringe.sort(key=comp)

    #Draws over discretized image according to the path found by the algorithm
    def draw_matrix(self, image, solutionPath):
        path_color = (159,59,212)
        # solutionPath = solutionPath[1:-1]
        for x in solutionPath:
            image[x[0]][x[1]] = path_color
        return image




    