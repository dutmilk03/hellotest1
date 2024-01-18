import cv2
import face_recognition
import numpy as np
import csv
import os
import glob
from datetime import datetime
cap = cv2.VideoCapture(0)

personl_name = "cee"
person_image = face_recognition.load_image_file("photos/cee.jpg")
persponl_face_encoding = face_recognition.face_encodings(person_image)[0]

personl2_name = "bank"
person2_image = face_recognition.load_image_file("photos/bank.jpg")
persponl2_face_encoding = face_recognition.face_encodings(person2_image)[0]

personl3_name = "jino"
personl3_image = face_recognition.load_image_file("photos/jino.jpg")
persponl3_face_encoding  = face_recognition.face_encodings(personl3_image)[0]

personl4_name = "kao"
personl4_image = face_recognition.load_image_file("photos/kao.jpg")
persponl4_face_encoding = face_recognition.face_encodings(personl4_image)[0]

personl5_name = "nakrop"
personl5_image = face_recognition.load_image_file("photos/nakrop.jpg")
persponl5_face_encoding = face_recognition.face_encodings(personl5_image)[0]

personl6_name = "Pan"
personl6_image = face_recognition.load_image_file("photos/Pan.jpg")
persponl6_face_encoding = face_recognition.face_encodings(personl6_image)[0]

personl7_name = "susi"
personl7_image = face_recognition.load_image_file("photos/susi.jpg")
persponl7_face_encoding = face_recognition.face_encodings(personl7_image)[0]

personl8_name = "pinky"
personl8_image = face_recognition.load_image_file("photos/pinky.jpg")
persponl8_face_encoding = face_recognition.face_encodings(personl8_image)[0]

personl9_name = "mint"
personl9_image = face_recognition.load_image_file("photos/mint.jpg")
persponl9_face_encoding = face_recognition.face_encodings(personl9_image)[0]

personl10_name = "bew"
personl10_image = face_recognition.load_image_file("photos/bew.jpg")
persponl10_face_encoding = face_recognition.face_encodings(personl10_image)[0]

personl11_name = "ingk 1"
personl11_image = face_recognition.load_image_file("photos/ingk 1.jpg")
persponl11_face_encoding = face_recognition.face_encodings(personl11_image)[0]

personl12_name = "ingk 2"
personl12_image = face_recognition.load_image_file("photos/ingk 2.jpg")
persponl12_face_encoding = face_recognition.face_encodings(personl12_image)[0]

personl13_name = "Jaja"
personl13_image = face_recognition.load_image_file("photos/Jaja.jpg")
persponl13_face_encoding = face_recognition.face_encodings(personl13_image)[0]

personl14_name = "Cherry"
personl14_image = face_recognition.load_image_file("photos/Cherry.jpg")
persponl14_face_encoding = face_recognition.face_encodings(personl14_image)[0]

personl15_name = "Kuk"
personl15_image = face_recognition.load_image_file("photos/Kuk.jpg")
persponl15_face_encoding = face_recognition.face_encodings(personl15_image)[0]

personl16_name = "plng"
personl16_image = face_recognition.load_image_file("photos/plng.jpg")
persponl16_face_encoding = face_recognition.face_encodings(personl16_image)[0]

personl17_name = "Soda"
personl17_image = face_recognition.load_image_file("photos/Soda.jpg")
persponl17_face_encoding = face_recognition.face_encodings(personl17_image)[0]

personl18_name = "pleng"
personl18_image = face_recognition.load_image_file("photos/pleng.jpg")
persponl18_face_encoding = face_recognition.face_encodings(personl18_image)[0]

personl19_name = "beam"
personl19_image = face_recognition.load_image_file("photos/beam.jpg")
persponl19_face_encoding = face_recognition.face_encodings(personl19_image)[0]

personl20_name = "Oon"
personl20_image = face_recognition.load_image_file("photos/Oon.jpg")
persponl20_face_encoding = face_recognition.face_encodings(personl20_image)[0]


known_face_encodings = [
    persponl_face_encoding,
    persponl2_face_encoding,
    persponl3_face_encoding,
    persponl4_face_encoding,
    persponl5_face_encoding,
    persponl6_face_encoding,
    persponl7_face_encoding,
    persponl8_face_encoding,
    persponl9_face_encoding,
    persponl10_face_encoding,
    persponl11_face_encoding,
    persponl12_face_encoding,
    persponl13_face_encoding,
    persponl14_face_encoding,
    persponl15_face_encoding,
    persponl16_face_encoding,
    persponl17_face_encoding,
    persponl18_face_encoding,
    persponl19_face_encoding,
    persponl20_face_encoding
]


known_face_names = [
personl_name,
personl2_name,
personl3_name,
personl4_name,
personl5_name,
personl6_name,
personl7_name,
personl8_name,
personl9_name,
personl10_name,
personl11_name,
personl12_name,
personl13_name,
personl14_name,
personl15_name,
personl16_name,
personl17_name,
personl18_name,
personl19_name,
personl20_name
]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+ '.csv', 'w+', newline ='')
exwriter = csv.writer(f)

while (True):
    check, frame = cap.read()
    if not check:
        print("Wrong")
        break
    resize_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_resize_frame = resize_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_resize_frame)
        face_encodings = face_recognition.face_encodings(rgb_resize_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
             matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
             name =''
             face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
             best_match_index = np.argmin(face_distance)
             if matches[best_match_index]:
                 name = known_face_names[best_match_index]

             face_names.append(name)
             if name in known_face_names:
                if name in students:
                  students.remove(name)
                  print(students)
                  current_time = now.strftime("%H-%M-%S")
                  exwriter.writerow([name, current_time])

    cv2.imshow("Video", frame)
    if (cv2.waitKey(1) & 0xFF ==ord("q")):
        break
cap.release()
cv2.destroyAllWindows()
f.close()