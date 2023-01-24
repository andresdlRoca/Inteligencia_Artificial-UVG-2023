import cv2
import numpy as np

class ImageReader(object):
    def __init__(self, image):
        self.image = cv2.imread(image)
        self.originalwidth, self.originalheight = self.image.shape[:2]
    
    def discretization(self, pixelated_height, pixelated_width):
        w, h = (pixelated_width,pixelated_height)
        discreetedimage = cv2.resize(self.image, (w,h), interpolation=cv2.INTER_LINEAR)
        outputImg = cv2.resize(discreetedimage, (self.originalwidth, self.originalheight), interpolation=cv2.INTER_NEAREST)

        cv2.imwrite("lab1discreet.bmp", outputImg)
        self.image = discreetedimage
        return self.image
    
    def coordinateFinder(self, image, upper_bound, lower_bound):
        mask = cv2.inRange(image, lower_bound, upper_bound)
        cords = np.where(mask == 255)
        return cords
    
    def upscaleImg(self, image):
        outputImg = cv2.resize(image, (self.originalwidth, self.originalheight), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite("lab1result.bmp", outputImg)
        cv2.imshow('Maze Result', outputImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

