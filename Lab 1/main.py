from imageReader import ImageReader
import numpy as np
import MazeSolverInterface

#BGR format
#Color detection for start
goalList = []
lower_red = np.array([0,0,200], dtype = "uint8")
upper_red = np.array([50,50,255], dtype= "uint8")

#Color detection for goals
lower_green = np.array([0,160,0], dtype="uint8")
upper_green = np.array([165,255,165], dtype="uint8")

#How many pixels will the output image be formed of
height, width = 15, 15 #lab1.bmp
imgReader = ImageReader("lab1.bmp")

imageMatrix = imgReader.discretization(height, width) #Image/Matrix already discretized
redStart = imgReader.coordinateFinder(imageMatrix, upper_red, lower_red) 
greenGoals = imgReader.coordinateFinder(imageMatrix, upper_green, lower_green)


# BFS solution
BFSsolver = MazeSolverInterface.BreadthFirstSolver(imageMatrix)
solvedMaze = BFSsolver.solve(redStart, greenGoals)
imgReader.upscaleImg(solvedMaze) #Shows and saves new image

#DFS Solution
DFSsolver = MazeSolverInterface.DepthFirstSolver(imageMatrix)
solvedMaze = DFSsolver.solve(redStart, greenGoals)
imgReader.upscaleImg(solvedMaze)

#A* Solution
AstarSolver = MazeSolverInterface.AStarSolver(imageMatrix)
solvedMaze = AstarSolver.solve(redStart, greenGoals)
imgReader.upscaleImg(solvedMaze)
