import time
import pkg_resources
from symspellpy import SymSpell, Verbosity
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pyttsx3
import symspellpy
from ggui import SimpleGUI
import threading

# Initialize GUI
gui = SimpleGUI()

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=3)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# Initialize OpenCV and related components
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("C:\\Users\\Indrajit\\PycharmProjects\\pythonProject1\\model\\keras_model.h5",
                        "C:\\Users\\Indrajit\\PycharmProjects\\pythonProject1\\model\\labels.txt")
offset = 20
imgSize = 300
labels = ["A", "B", "C", "D", "ok"]
texttospeech = pyttsx3.init()
previousindex = 0
Finalstring = ""


def remove_adjacent_duplicates(s):
    if not s:
        return s

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 4:
                result.append(current_char)
            current_char = char
            count = 1

    if count > 4:
        result.append(current_char)

    return ''.join(result)





def main_loop():
    global previousindex, Finalstring

    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
                imgCropShape = imgCrop.shape
                aspectRatio = h / w
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

                prediction, index = classifier.getPrediction(imgWhite, draw=False)

                if index == 4:

                    gui.clear_text()
                    inputterm = remove_adjacent_duplicates(Finalstring.lower())
                    suggestions = sym_spell.lookup(inputterm, Verbosity.CLOSEST)
                    gui.update_text("printing.....")
                    gui.update_text(f"Total suggestions: {len(suggestions)}")
                    gui.update_text(inputterm)
                    gui.update_text("suggestions:")

                    print(inputterm)
                    for suggestion in suggestions:
                        gui.update_text(str(suggestion))

                    if previousindex != index:
                        Finalstring += labels[previousindex]
                else:
                    previousindex = index
                    time.sleep(0.15)
                    
                cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                              (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
                cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 255, 255), 1)
                cv2.rectangle(imgOutput, (x - offset, y - offset),
                              (x + w + offset, y + h + offset), (255, 0, 255), 4)
                # cv2.imshow("ImageCrop", imgCrop)
                # cv2.imshow("ImageWhite", imgWhite)

            winname = "Image"
            cv2.namedWindow(winname)  # Create a named window
            cv2.moveWindow(winname, 1500, 30)  # Move it to (40,30)
            cv2.imshow(winname, imgOutput)
        # cv2.imshow("Image", imgOutput)

        key = cv2.waitKey(1)
        if key == ord('q'):  # Press 'q' to quit the loop
            break
        if key == ord('r'):
           Finalstring=""

    cap.release()
    cv2.destroyAllWindows()


# Run the main loop in a separate thread to keep the GUI responsive
thread = threading.Thread(target=main_loop)
thread.start()

# Run the GUI
gui.run()
