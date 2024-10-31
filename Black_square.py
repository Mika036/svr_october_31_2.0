import cv2
cap = cv2.VideoCapture(0)

# list_example = [0, 1, 2, 3]
# print(list_example[1:3])
# exit()

while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape
    frame[height - 100:, :100] = [12, 0, 0]
    frame[height - 100:, width - 100:] = [43, 2, 0]
    frame[:100, :100] = [0, 0, 0]
    frame[:100, width - 100:] = [0, 212, 0]
    frame[height - 290: height - 190, width - 370: width - 270] = [256, 256, 256]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    print(key)
    if key == 32:
        break
cv2.destroyAllWindows()
cap.release()