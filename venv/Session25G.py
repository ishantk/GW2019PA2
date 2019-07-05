import cv2, datetime

video = cv2.VideoCapture(0)

frames = 0

while True:

    check, frame = video.read()

    frames = frames + 1

    print(frame)

    cv2.imshow("MyVideo", frame)

    # 1 means 1 milli second
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

print(">> Frames Captured:",frames)

# https://opencv.org/
# https://docs.opencv.org/master/d9/df8/tutorial_root.html
