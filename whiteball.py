import os
import glob
import time
import SimpleCV
from SimpleCV import *

display = SimpleCV.Display()
c = SimpleCV.Camera()
normaldisplay = True

my_images_path = "C:\Users\SAIKAT\Desktop\escapist\escapist simulator\export" 
extension = "*.bmp"
if not my_images_path:
        path = os.getcwd() 
else:
        path = my_images_path
imgs = list()
directory = os.path.join(path, extension)
files = glob.glob(directory)
time.sleep(3)

while display.isNotDone():

	if display.mouseRight:
		normaldisplay = not(normaldisplay) 
	
	img = c.getImage().flipHorizontal()
	dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
	segmented = dist.stretch(200,255)
	
	bl = segmented.findBlobs()
	if bl:
		circle = bl.filter([b.isCircle(0.2) for b in bl])
		if circle:
			img.drawCircle((circle[-1].x, circle[-1].y), circle[-1].radius(),SimpleCV.Color.RED,5)

	if normaldisplay:
		img.show()
	else:
		segmented.show()
