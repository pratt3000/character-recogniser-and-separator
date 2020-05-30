from cv2 import cv2
import numpy as np
import time

# read  full image
im = cv2.imread("testCases/p.jpeg", 0)
# adjust colours
ret, thresh1 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
# get boxes
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# loop for all boxes
for cnt in contours:
    # get origin and width height
    x, y, w, h = cv2.boundingRect(cnt)
    # bound the images
    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
i = 0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # ignore the noises and save the images which are of normal size(character)
    if w > 100 and h > 100:
        # save individual images in another place
        cv2.imwrite(
            "IndividualImages/" + str(i) + ".jpg", thresh1[y : y + h, x : x + w]
        )
        i = i + 1
# error dk what
cv2.namedWindow("BindingBox", cv2.WINDOW_NORMAL)
cv2.imshow("BindingBox", im)
# just to see
time.sleep(5)
