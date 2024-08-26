import cv2
import numpy as np
# Load the image
image = cv2.imread('C:\\Users\\Murtaza\\Downloads\\James.jpg')

# Convert the image to Lab color space for better luminance control
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Apply Non-Local Means Denoising to the entire image for smoothing (wrinkle removal)
smoothed_lab = cv2.fastNlMeansDenoisingColored(lab, None, 5, 5, 7, 21)

# Generate a subtle noise pattern (adjust strength as needed)
noise = np.random.normal(0, 10, image.shape).astype(np.uint8)

# Create a mask for the image
mask = np.zeros_like(image)

# Apply the noise to the mask
noisy_mask = cv2.add(mask, noise)

# Combine the noisy mask with the smoothed image using a blending mode
alpha = 0.1  # Adjust the strength of the effect
blended_image = cv2.addWeighted(smoothed_lab, 1-alpha, noisy_mask, alpha, 0)

# Convert back to BGR color space
output_image = cv2.cvtColor(blended_image, cv2.COLOR_LAB2BGR)

# Save the result
cv2.imwrite('output_image.jpg', output_image)
