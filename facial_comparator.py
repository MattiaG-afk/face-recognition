import face_recognition

path1 = str(input("Insert the file name of the known photo: "))
path2 = str(input("Insert the file name of thew unknown photo: "))

photo1 = face_recognition.load_image_file(path1)
photo2 = face_recognition.load_image_file(path2)

photo1_encoding = face_recognition.face_encodings(photo1)[0]
photo2_encoding = face_recognition.face_encodings(photo2)[0]

face_distance = face_recognition.face_distance([photo1_encoding], photo2_encoding)
match = True if face_distance[0] <= 0.6 else False

print(f"Are the people in the two pictures the same? { match }")
print(f"Face distance from 0 to 1: { match }")