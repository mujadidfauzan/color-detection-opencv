import cv2 as cv
from PIL import Image
from util import get_limits

blue = [255, 0, 0]  # blue dalam BGR
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=blue)

    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    # print(bbox)
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv.imshow('img', frame)
    cv.imshow('frame', mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
