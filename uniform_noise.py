import cv2
import numpy as np

def add_uniform_noise(image):
    row, col, ch = image.shape
    uniform_noise = np.random.uniform(-50, 50, (row, col, ch)).astype('uint8')
    noisy_image = cv2.add(image, uniform_noise)
    return noisy_image

def reduce_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Load the image
image = cv2.imread('image.jpg')
noisy_image = add_uniform_noise(image)
denoised_image = reduce_noise(noisy_image)

# Display the images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
