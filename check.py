import cv2
import mediapipe as mp
import numpy as np
import pyttsx3  # For Text-to-Speech

# Initialize MediaPipe Hands and TTS Engine
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
engine = pyttsx3.init()

# Define simple sign-to-text dictionary
sign_dict = {
    "Hello": [4, 8, 12, 16, 20],  # Open palm, fingers extended
    "Thank You": [4, 8, 12],  # Thumb touching chin, moving outward
    "Ice Cream": [4, 8],  # Thumb and index extended (like holding a cone)
    "Yes": [0, 4],  # Fist opening and closing (check thumb movement)
    "No": [4, 8, 12],  # Index and middle extended, thumb moving
    "Goodbye": [4, 8, 12, 16, 20],  # Open palm, moving side to side
    "Sorry": [0],  # Closed fist moving in circles
    "Love": [4, 8, 20],  # Thumb, index, pinky extended (rock sign 🤘)
    "Please": [0, 1],  # Open palm moving in circles
    "Help": [0, 4],  # Fist over open palm
    "Food": [4, 8],  # Fingers touching lips
}


# Function to recognize hand signs
def recognize_sign(landmarks):
    fingers = []
    
    for tip_id in [4, 8, 12, 16, 20]:
        if landmarks[tip_id][1] < landmarks[tip_id - 2][1]:  # Compare y-coordinates
            fingers.append(tip_id)

    for sign, pattern in sign_dict.items():
        if set(pattern).issubset(set(fingers)):
            return sign
    return None

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)
    

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
            # Convert landmarks to (x, y) positions
            landmarks = [(lm.x * w, lm.y * h) for lm in hand_landmarks.landmark]

            # Recognize sign
            detected_sign = recognize_sign(landmarks)

            # Draw bounding box and text if a sign is detected
            if detected_sign:
                x_min, y_min = min(landmarks, key=lambda p: p[0])[0], min(landmarks, key=lambda p: p[1])[1]
                x_max, y_max = max(landmarks, key=lambda p: p[0])[0], max(landmarks, key=lambda p: p[1])[1]

                cv2.rectangle(frame, (int(x_min)-20, int(y_min)-20), (int(x_max)+20, int(y_max)+20), (0, 255, 0), 2)
                cv2.putText(frame, detected_sign, (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Convert text to speech
                engine.say(detected_sign)
                engine.runAndWait()

    # Display output
    cv2.imshow("Sign Language Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
