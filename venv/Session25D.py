import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("==check==")
print(check)

print("==frame==")
print(frame)

print(type(frame))

time.sleep(3)

video.release()
cv2.destroyAllWindows()