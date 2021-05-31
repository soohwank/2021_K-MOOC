import cv2
import os
import numpy as np

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img_color = cv2.imread('KITTI_resized.png')

# Check if image loading is successful
if img_color is None:
    print('Error: No image exists')
    exit(1)

# color conversion
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('KITTI_BW.png', img_gray)

# ROI
x = 485
y = 119
width = 10
height = 10
roi = img_gray[y:y+height, x:x+width]
rows, cols = roi.shape
print(roi.shape)

for row in range(0, rows):
    for col in range(0, cols):
        print(roi[row, col], end =" ")
        if col == cols - 1:
            print('\\\\ \n', end ="")
        else:
            print('& ', end ="")

# Display the image in a window
cv2.imshow('KITTI', roi)

# Wait for a key to be pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
