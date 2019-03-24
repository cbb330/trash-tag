import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

def get_N_Face_Caps(n):
    # Access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    num = 0 
    while num<10:
        face_detected = False
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            if w > 0:
                face_detected = True
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)

        if face_detected:
            cv2.imwrite('../assets/target_images/target' + str(num) + '.jpg', frame)
            num = num + 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    
