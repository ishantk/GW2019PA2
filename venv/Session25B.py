import cv2
img = cv2.imread("ibises.jpg", 1)
cv2.imshow("AnyTitleName", img)

# Wait till user will not press any key on the keyboard
# cv2.waitKey(0)

# Wait for 3 secs and destroy after 3 secs
cv2.waitKey(3000)
cv2.destroyAllWindows()

# Try Creating your own numpy array of pixels and show it as image
# Pixel -> [R G B] | R/G/B  is from 0 to 255