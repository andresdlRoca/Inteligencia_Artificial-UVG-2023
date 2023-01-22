from imageReader import ImageReader
import numpy as np
import MazeSolverInterface
green = [0,255,0] #Goal
red = [254,6,6] #Start
imgReader = ImageReader("lab1.bmp", 50, 50)

imageMatrix = imgReader.image2Matrix()

# print(imageMatrix[5])

problemSolver = MazeSolverInterface
problemSolver(imageMatrix)

goals = problemSolver.coordinateFinder(green)
start = problemSolver.coordinateFinder(red)

BFSsolver = problemSolver.BreadthFirstSolver.solve(imageMatrix, start=start, end=goals)


# # Unique elements in nested tuple
# # Using nested loop + set()
# res = []
# temp = set()
# for inner in imageMatrix:
#         for ele in inner:
#             if not ele in temp:
#                 temp.add(ele)
#                 res.append(ele)
 
# # printing result
# print("Unique elements in nested tuples are : " + str(res))



