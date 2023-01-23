import cv2
import numpy as np

class ImageReader(object):
    def __init__(self, image):
        self.image = cv2.imread(image)
    
    def discretization(self, pixelated_height, pixelated_width):
        height, width = self.image.shape[:2]
        w, h = (pixelated_width,pixelated_height)
        discreetedimage = cv2.resize(self.image, (w,h), interpolation=cv2.INTER_LINEAR)
        outputImg = cv2.resize(discreetedimage, (width, height), interpolation=cv2.INTER_NEAREST)

        cv2.imwrite("lab1discreet.bmp", outputImg)
        # cv2.imshow("input", self.image)
        # cv2.imshow("output", outputImg)
        # cv2.waitKey(0)
        self.image = discreetedimage
        return self.image
    
    def coordinateFinder(self, image, upper_bound, lower_bound):
        mask = cv2.inRange(image, lower_bound, upper_bound)
        return mask

