import cv2
import numpy as np

def add_speckle_noise(image):
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    noisy_image = image + image * gauss
    return noisy_image

def reduce_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Load the image
image = cv2.imread('images.jpg')
noisy_image = add_speckle_noise(image)
denoised_image = reduce_noise(noisy_image)

# Display the images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
