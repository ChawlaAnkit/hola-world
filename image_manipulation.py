
# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image_color = cv2.imread('nw_image.jpg',0)
image_unchanged = cv2.imread("image.png",-1)
cv2.imshow("nw_image",image_color)
cv2.imshow("hello",image_unchanged)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("nw_image.jpg",image)
  
# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))

