''' Face tracking '''

import cv2

# Load the pre-trained face cascade
FACE_CLASSIFIER = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(video_frame):
    ''' Draw a bounding box around the face(s)'''

    gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = FACE_CLASSIFIER.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))

    # Draw bounding boxes around the faces
    # The (x, y) coordinates represent the top-left corner of the rectangle, (x+w, y+h) represent the bottom-right corner.
    # The color (255, 0, 0) blue,
    # 2 is the thickness of the rectangle lines.
    for (x, y, w, h) in faces:
        cv2.rectangle(video_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return faces

if __name__ == "__main__":
    # Open a connection to the webcam (0 is usually the default webcam)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame by frame
        result, video_frame = video_capture.read()

        # Break if the frame is not read successfully
        if result is False:
            break

        # Draw bounding around the face(s)
        faces = detect_bounding_box(video_frame)

        # Display the frame in a window named "Face tracking"
        cv2.imshow("Face tracking", video_frame)

        # Exit video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam and close the OpenCV window
    video_capture.release()
    cv2.destroyAllWindows()
