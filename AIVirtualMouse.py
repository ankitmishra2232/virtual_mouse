import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
############################
wCam,hCam =640,480
############################

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
pTime =0
detector = htm.handDetector(maxHands=1)


while True:
    #1. find hand Landmarks

    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #2. Get the tip of the index and middle fingers
    #3. Check which fingers are up
    #4. Only Index Finger : moving mode
    #5. Convert Coordinates
    #6. Smoothen Value
    #7. Move Mouse
    #8. Both Index and middle fingres are up: Clicking mode
    #9. Find Distance between fingures
    #10. Click mouse if distance short

    #11. Frame Rate
    cTime =time.time()
    fps =1/(cTime -pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,(0, 255, 0), 5)
    #12. Display
    cv2.imshow("image",img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
