import time

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Initialize hand detector
detector = HandDetector(maxHands=2)
offset = 20
imgSize = 300
folder = "C:\\Users\\Indrajit\\PycharmProjects\\pythonProject1\\data\\ok"
counter =0
while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture image")
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Ensure the crop coordinates are within the image bounds
        y1, y2 = max(0, y - offset), min(img.shape[0], y + h + offset)
        x1, x2 = max(0, x - offset), min(img.shape[1], x + w + offset)

        imgCrop = img[y1:y2, x1:x2]
        imgCropShape = imgCrop.shape

        if imgCropShape[0] == 0 or imgCropShape[1] == 0:
            print("Error: Image crop is empty")
            continue

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        aspectRatio = h / w

        try:
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)
        except Exception as e:
            print(f"Error during resizing: {e}")
            continue

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('q'):  # Press 'q' to quit the loop
        break
    if key == ord('s'):
        counter+=1

        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)

cap.release()
cv2.destroyAllWindows()
