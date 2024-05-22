import cv2

image = cv2.imread('city.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_invert = 255 - image_gray

blurred = cv2.GaussianBlur(image_invert, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(image_gray, inverted_blurred, scale=256.0)

cv2.imshow("Original", image)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)