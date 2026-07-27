import cv2
import os

from deepface import DeepFace

# Webcam
cap = cv2.VideoCapture(0)

# Haarcascade detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Known faces folder
known_faces_dir = "known_faces"

known_faces = []

# Load known faces
for file in os.listdir(known_faces_dir):

    if file.endswith(".jpg") or file.endswith(".png"):

        path = os.path.join(known_faces_dir, file)

        name = os.path.splitext(file)[0]

        known_faces.append({
            "name": name,
            "path": path
        })

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Process every detected face
    for (x, y, w, h) in faces:

        # Crop face
        face_crop = frame[y:y+h, x:x+w]

        detected_name = "Unknown"

        try:

            result = DeepFace.find(
                img_path=face_crop,
                db_path="known_faces",
                enforce_detection=False,
                silent=True
            )

            if len(result) > 0 and not result[0].empty:

                identity = result[0].iloc[0]['identity']

                detected_name = os.path.basename(identity).split('.')[0]

            else:
                detected_name = "Unknown"

        except Exception as e:
            print(e)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        # Draw name
        cv2.putText(
            frame,
            detected_name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Show frame
    cv2.imshow("Real-Time Face Recognition", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()