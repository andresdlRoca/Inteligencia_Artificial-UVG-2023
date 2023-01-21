from PIL import Image

class ImageReader(object):
    def __init__(self, image, width, height):
        self.image = Image.open(image)
        self.width = width
        self.height = height
        
        self.image.thumbnail((self.width,self.height)) #Image resizing
        self.image.save('lab1new.bmp')


    def image2Matrix(self):
        width, height = self.image.size
        matrix = []
        print(self.image.size)
        for y in range(height):
            row = []
            for x in range(width):
                pixel = self.image.getpixel((y,x))
                row.append(pixel)
            matrix.append(row)
        return matrix