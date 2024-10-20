import numpy as np
import cv2

def get_color_at_point(x, y, x1, y1, x2, y2, color1, color2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return color1
    t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))
    r = int(color1[0] + t * (color2[0] - color1[0]))
    g = int(color1[1] + t * (color2[1] - color1[1]))
    b = int(color1[2] + t * (color2[2] - color1[2]))
    return (r, g, b)

width, height = 500, 500
x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter second point (x2 y2): ").split())
color1 = tuple(map(int, input("Enter first color (R G B): ").split()))
color2 = tuple(map(int, input("Enter second color (R G B): ").split()))

image = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        color = get_color_at_point(x, y, x1, y1, x2, y2, color1, color2)
        image[y, x] = color

cv2.imwrite('gradient.png', image)
cv2.imshow('Gradient', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
