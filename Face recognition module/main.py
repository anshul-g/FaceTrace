import face_recognition
import datetime
import cv2
import numpy as np
import os
import pandas as pd
import time
from utils_csv import append_df_to_csv

video_capture = cv2.VideoCapture(0)

# Initializing lists
known_face_encodings = []
known_face_roll_no = []
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
attendance_record = set([])
roll_record = {}

# Rows in log file
name_col = []
roll_no_col = []
time_col = []

df = pd.read_excel("database" + os.sep + "people_db.xlsx")

for key, row in df.iterrows():

    roll_no = row['roll_no']
    name = row['name']
    image_path = row['image']
    roll_record[roll_no] = name

    student_image = face_recognition.load_image_file("database" + os.sep + image_path)
    student_face_encoding = face_recognition.face_encodings(student_image)[0]

    known_face_encodings.append(student_face_encoding)
    known_face_roll_no.append(roll_no)


while True:
    # Grab a single frame of video
    vid, frame = video_capture.read()

    # Resizing frame and then converting to RGB color (for face_recognition module)
    resized_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    modified_frame = resized_frame[:, :, ::-1]
    
    if process_this_frame:
        
        locations = face_recognition.face_locations(modified_frame)
        encodings = face_recognition.face_encodings(modified_frame, locations)

        face_names = []

        # Checking if face is present in database
        for face_encoding in encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match = np.argmin(distances)

            if matches[best_match]:
                roll_no = known_face_roll_no[best_match]

                # logging information related to matched face
                name = roll_record[roll_no]
                if roll_no not in attendance_record:
                    attendance_record.add(roll_no)
                    print(name, roll_no)
                    name_col.append(name)
                    roll_no_col.append(roll_no)
                    curr_time = time.localtime()
                    curr_clock = time.strftime("%H:%M:%S", curr_time)
                    time_col.append(curr_clock)

            face_names.append(name)

    #process_this_frame = not process_this_frame

    # Showing a rectangle and label around the face
    for (top, right, bottom, left), name in zip(locations, face_names):

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame, (left, bottom - 35),(right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),font, 1.0, (255, 255, 255), 1)

    # Final image output
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Storing data in attendance file
data = {'Name': name_col, 'Roll No.': roll_no_col, 'Time': time_col}

now = datetime.datetime.now()
dt_string = now.strftime("%d-%m-%Y %H_%M")

today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")
curr_time = time.localtime()
curr_clock = time.strftime("%c", curr_time)
date_info = curr_clock.replace(":","_")
log_file_name = "Attendance record " + str(dt_string) + ".csv"

# Adding data to csv file
append_df_to_csv(log_file_name, data)

video_capture.release()
cv2.destroyAllWindows()

