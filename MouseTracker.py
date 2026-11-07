
import cv2
import os

# Camera
cam = cv2.VideoCapture(0)

# XML file paths
base_path = r"F:\AIOLearn-Internship\Machine Learning\10 projects\MouseTracker"

eye_path = os.path.join(base_path, "haarcascade_eye.xml")
face_path = os.path.join(base_path, "haarcascade_frontalface_default.xml")

# Load Haar Cascade models
eye_model = cv2.CascadeClassifier(eye_path)
face_model = cv2.CascadeClassifier(face_path)

# Check XML files
if eye_model.empty():
    print("Error: Eye cascade file not found!")
    exit()

if face_model.empty():
    print("Error: Face cascade file not found!")
    exit()

# Check camera
if not cam.isOpened():
    print("Error: Camera could not be opened!")
    exit()

loop = True

while loop:

    ret, img = cam.read()

    if not ret:
        print("Error: Cannot read from camera!")
        break

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_model.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    imgout = img.copy()

    for (x, y, w, h) in faces:

        # Draw face rectangle
        cv2.rectangle(
            imgout,
            (x, y),
            (x + w, y + h),
            (0, 250, 0),
            3
        )

        # Crop face region
        gray_face = gray[y:y+h, x:x+w]

        # Detect eyes inside face
        eyes = eye_model.detectMultiScale(
            gray_face,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        ic = 0

        for (xe, ye, we, he) in eyes:

            # Draw eye rectangle
            cv2.rectangle(
                imgout,
                (xe + x, ye + y),
                (xe + x + we, ye + y + he),
                (0, 0, 250),
                2
            )

            ic += 1

            # Detect maximum two eyes
            if ic == 2:
                break

    # Show output
    cv2.imshow("Face and Eye Detection", imgout)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        loop = False

# Release camera
cam.release()
cv2.destroyAllWindows()
