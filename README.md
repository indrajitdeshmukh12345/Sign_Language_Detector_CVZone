
# Sign_Language_Detector_CVZone

This project demonstrates a hand gesture recognition system using OpenCV, CvZone, Customtkinter and symspellpy. The system captures live video from a webcam, processes the video to detect hand gestures, displays the live video feed and recognized gestures along with real-time spell checking and word suggestions.


## Installation

```requirements.txt  ```
contains all the Python libraries required.
can be installed using:
```bash
  pip install -r requirements.txt
```
Using 
[python version 3.80](https://www.python.org/downloads/release/python-380/)
opencv-python, cvzone, pyttsx3,
   symspellpy,
   numpy

    
## Dataset

Once the images are collected using ```datacolector.py  ```, Modle is trained using 
[Teachable Machine](https://teachablemachine.withgoogle.com/). TensorFlow kereas modle is used.
```keras_model.h5``` 
This modle is trained to recognize hand gestures for "a,b,c,d".this modle is not complete 
## Screenshots

![App Screenshot](https://github.com/indrajitdeshmukh12345/Sign-language-/assets/46133820/7e6d0aa5-cfbf-4f45-8c6c-551a8c3f783a
)

![Spell correction](https://github.com/indrajitdeshmukh12345/Sign-language-/assets/46133820/88c0e4de-7b59-479a-9559-0873051a7fef)

![hand_sign](https://github.com/indrajitdeshmukh12345/Sign-language-/assets/46133820/c3576f1a-c74c-4172-8d10-3a219bb6e20c)


## File Structure

- ```test2.py  ``` The main script that captures video, processes gestures, and updates the GUI
- ```ggui.py  ``` Contains the SimpleGUI class for creating and managing the Tkinter GUI.
- Modle Directory: coontins ```keras_model.h5 modle``` and ```labels.txt``` lables 
- ```requirements.txt  ``` List of Python packages required to run the project.
- ```README.md```This File

- ```SymSpell.cs``` ```frequency_dictionary_en_82_765.txt ``` ``` EditDistance.cs``` requirements for SymSpell library 
## Documentation

[customtkinter](https://customtkinter.tomschimansky.com/documentation/)

[symspellpy](https://symspellpy.readthedocs.io/en/latest/api/index.html)

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any features, bug fixes, or enhancements.

Please adhere to this project's `code of conduct`.

