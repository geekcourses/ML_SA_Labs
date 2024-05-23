import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys



# ---------------------------- Read the image file --------------------------- #
# image = cv.imread('./smiley-300x273.png')

# print( type(image) )
# print(image.shape) (h, w, 3)

# -------------------------------- Show image -------------------------------- #
# cv.imshow("Display window", image)

# k = cv.waitKey(0)

# ------------------------------  BGR Colors note ----------------------------- #
# Red:    0 - 255
# Green:  0 - 255
# Blue:   0 - 255

# Red: ( 0, 0, 255 )
# Purple = (255, 0, 255)
# Yellow = (255, 255)
# Red    = (0,0,0)
# White  = (255,255,255)
# Gray   = (127, 127, 127)

# ------------------------------- Create Image ------------------------------- #

# Create a blank image 4x6 with white (255,255,255) pixels
# image = np.full((6, 4, 3), 255, dtype=np.uint8)

### Set the pixel values for the lines of the number 0 to red BGR:( 0, 0, 255)

## Set Top line pixels to red ()
# image[0, 0] = [255,0,255]
# image[0, 1] = [0,0,255]
# image[0, 2] = [0,0,255]
# image[0, 3] = [0,0,255]

# ## Bottom line
# image[5, 0] = [0,0,255]
# image[5, 1] = [0,0,255]
# image[5, 2] = [0,0,255]
# image[5, 3] = [0,0,255]

# ## Left column
# image[1:5, 0] = [0,0,255]

# ## Right Column
# image[1:5, 3] = [0,0,255]

# # Save the image
# cv.imwrite('number_0.png', image)


# ------------------------------- Display Image ------------------------------ #


# Read the image and display it using matplotlib
# image = plt.imread('number_0.png')
# plt.imshow(image)
# plt.show()