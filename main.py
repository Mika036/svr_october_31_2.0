import cv2
from pprint import *
import sys
import numpy
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    cv2.waitKey(1)
    print(list(frame))
    print(ret)
    for el in frame:
        for i in el:
            print(i, end='')
        print()

    break