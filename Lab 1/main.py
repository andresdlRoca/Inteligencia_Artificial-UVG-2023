from imageReader import ImageReader

imgReader = ImageReader("lab1.bmp", 50,50)

imageMatrix = imgReader.image2Matrix()

print(imageMatrix)


