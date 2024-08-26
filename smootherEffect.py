import cv2
import numpy as np
# Load the image
image = cv2.imread('C:\\Users\\Murtaza\\Downloads\\James.jpg')

# Get the width and height of the image
height, width = image.shape[:2]

# Apply Non-Local Means Denoising to the entire image for smoothing
smoothed_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Save the result
cv2.imwrite('output_image.jpg', smoothed_image)