import random
import cv2
from PIL import Image


def add_noise(img):

	# Getting the dimensions of the image
	row , col = img.shape
	
    #randomly putting 10000 salt
	number_of_pixels = 150000
	for i in range(number_of_pixels):
	
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to white
		img[y_coord][x_coord] = 255
		

    #randomly putting 10000 salt
	number_of_pixels = 150000
	for i in range(number_of_pixels):
	
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to black
		img[y_coord][x_coord] = 0
		
	return img

# salt-and-pepper noise can
# be applied only to grayscale images
# Reading the color image in grayscale image
img = cv2.imread('cameraman-og.png',
				cv2.IMREAD_GRAYSCALE)

#Storing the image
cv2.imwrite('saty-cameraman.jpg',
			add_noise(img))
def main():
    img = Image.open("salty-cameraman.jpg")
    img.show()

main()