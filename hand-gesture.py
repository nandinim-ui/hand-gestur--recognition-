import cv2
import time
import cvzone
from cvzone.HandTrackingModule import HandDetector

pTime = 0
detector = HandDetector(detectionCon=0.8, maxHands=1)
##########################
wCam, hCam = 400, 200
##########################

cap = cv2.VideoCapture(0)
cap.set(2, wCam)
cap.set(1, hCam)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if len(hands) == 1:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)

        if fingerUp == [0, 1, 0, 0, 1]:
            cv2.putText(frame, 'ROCK', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'ROCK'
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'VICTORY', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'VICTORY'
        elif fingerUp == [1, 0, 0, 0, 0]:
            cv2.putText(frame, 'OK', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'OK'
        elif fingerUp == [1, 1, 0, 0, 1]:
            cv2.putText(frame, 'LOVE YOU', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'LOVE YOU'
        elif fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'BYE', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'BYE'
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'HELLO', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)
            gesture = 'HELLO'
        else:
            gesture = 'UNKNOWN'

        cv2.putText(frame, gesture, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, (30, 30, 30), 2, cv2.LINE_AA)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

cap.release()
cv2.destroyAllWindows()

