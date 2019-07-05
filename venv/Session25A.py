import cv2
print(cv2.__version__) # 4.1

# 1 means read image as colored image | 0 : BW
img = cv2.imread("ibises.jpg", 1)
print("====Image====")
print(img)
print("====Image Type====")
print(type(img))
print("====Image Shape====")
print(img.shape) # 2000, 2500, 3

"""
[
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [],
    [] 
]
"""

print("==1st Pixel of Image===")
print(img[0][0])

print(len(img[0]))      #
