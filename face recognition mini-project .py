import cv2 
from google.colab.patches import cv2_imshow
from google.colab import files

def detect_faces(image):
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display number of faces detected
    num_faces = len(faces)
    print("Number of faces detected:", num_faces)

    # Display the image with rectangles
    cv2_imshow(image)

def process_images(image_files):
    for filename in image_files:
        print('Processing image file:', filename)
        image = cv2.imread(filename)

        if image is None:
            print("Error: Unable to load image file:", filename)
            continue

        detect_faces(image)

def main():
    # Upload image files
    print("Upload image files:")
    uploaded = files.upload()
    image_files = list(uploaded.keys())

    # Process uploaded image files
    if len(image_files) > 0:
        process_images(image_files)
    else:
        print("No image files uploaded.")

if __name__ == "__main__":
    main()
