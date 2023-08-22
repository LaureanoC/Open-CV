import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    
     while True:
        ret, frame = cap.read()
        if ret == False:
            break

        #rectangulo if(x1 < 320 and y1 < 240):
        cv2.rectangle(frame, (320,240), (640,0), (0,255,0), 1)
    
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:    
    # Accediendo al valor de los puntos por su índice
            index = [4, 8, 12, 16, 20]
            for hand_landmarks in results.multi_hand_landmarks:
                for (i, points) in enumerate(hand_landmarks.landmark):
                    if i in index:
                        x = int(points.x * width)
                        y = int(points.y * height)
                        cv2.circle(frame, (x, y), 3,(255, 0, 255), 3)
                
        if results.multi_hand_landmarks is not None:    
    # Accediendo a los puntos de referencia, de acuerdo a su nombre
            for hand_landmarks in results.multi_hand_landmarks:
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
                
                if(x1 < 320 and y1 < 240):
                    print('X: ', x1)
                    print('Y: ', y1)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()