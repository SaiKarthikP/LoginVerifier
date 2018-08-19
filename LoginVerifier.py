import face_recognition
import cv2
import ctypes
import time

# Get a reference to default webcam #0 
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
p1_image = face_recognition.load_image_file("IDs/p1.jpg")
p1_face_encoding = face_recognition.face_encodings(p1_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [p1_face_encoding]

text_file = open('IDs/people.txt', 'r')

p1name = text_file.readline()
known_face_names = [p1name]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
isp1 = False
videoWriterCreated = False
instantiateWriter = False

# Time till app times out
timeout = time.time() + 5
# Time when app should start capturing video
captureTime = time.time() + 2

while time.time() < timeout:
	# if not person1 and past captureTime then instantiate videoWriter 
    if instantiateWriter:
        # define codec and create videowriter object
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        out = cv2.VideoWriter('intruders/output_' + str(time.time()) + '.avi', fourcc, 30.0,
                              (int(video_capture.get(3)), int(video_capture.get(4))))
        videoWriterCreated = True
        instantiateWriter = False
        out.write(frame)

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition module uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if name == p1name:
                isp1 = True
                break

        face_names.append(name)

    if isp1:
        break
    else:
        if time.time() > captureTime:
            if videoWriterCreated:
				# write frame to video
                out.write(frame)
            else:
                instantiateWriter = True

	# Display
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
if isp1:
    ctypes.windll.user32.MessageBoxW(0, "Hi " + p1name + ". Sorry to bother you.", "Face Recognition Verifier", 1)
    pass

else:
    out.release()
	#lock out user/workstation
    ctypes.windll.user32.LockWorkStation()