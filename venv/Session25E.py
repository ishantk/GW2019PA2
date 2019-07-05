import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("==check==")
print(check)

print("==frame==")
print(frame)

print(type(frame))

cv2.imshow("MyFrame", frame)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()