import cv2
# img = cv2.imread("ibises.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("ibises.jpg", 1)


# resizedImg = cv2.resize(img, (400, 400))

shape = img.shape
# print(shape)
resizedImg = cv2.resize(img, (shape[1]//2, shape[0]//2))

cv2.imshow("AnyTitleName", resizedImg)

cv2.imwrite("MyIbises.jpg", resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()