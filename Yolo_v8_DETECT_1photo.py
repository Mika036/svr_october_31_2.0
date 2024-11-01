from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
from pprint import pprint

model = YOLO('best.pt')

while True:
    img = cv2.imread('photo.jpg')

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img, conf=0.05)

    for r in results:

        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

    img = annotator.result()
    cv2.imshow('Yolo V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cv2.destroyAllцWindows()