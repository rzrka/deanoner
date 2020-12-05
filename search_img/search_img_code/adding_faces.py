import cv2, os
import numpy as np
import face_recognition
import copy


def detected_fc(image):
        fac_loc = face_recognition.face_locations(image)[0]
        fac_encode = face_recognition.face_encodings(image)[0]
        return fac_encode

def added_face(encode_face_list):
    encode_image_main_new = copy.deepcopy(encode_image_main)
    encode_face_list_new = []
    for i in range(128):
        count = 0
        for j in range(len(encode_face_list)):
            count += encode_face_list[j][i]
        encode_face_list_new.append((count / len(encode_face_list)))

    for i in range(len(encode_image_main_new)):
        encode_image_main_new[i] = encode_face_list_new[i]
    encode_face_list[0] = encode_face_list_new
    return encode_face_list[0]


encode_face_list = []
none_detec_list = []
res_list = [] #список всех лиц

image_main = cv2.cvtColor(cv2.imread('../test_img/main.jpg'), cv2.COLOR_BGR2RGB)
encode_image_main = detected_fc(image_main)
encode_face_list.append(encode_image_main)

#перебор всех фалов из папки
path = '../test_img/'
image_paths = [os.path.join(path, f) for f in os.listdir(path)]
for el_image in image_paths:
    try:
        if el_image.endswith('.jpg') or el_image.endswith('.jpeg'):
            image_check_fc = cv2.cvtColor(cv2.imread(el_image), cv2.COLOR_BGR2RGB)
            encode_check_fc = detected_fc(image_check_fc)
            results = face_recognition.compare_faces([encode_image_main], encode_check_fc, tolerance=0.55)
            if results[0]:
                res_list.append(el_image)
                encode_face_list.append(encode_check_fc)
    except IndexError:
        none_detec_list.append(el_image)
        continue

result_adding_face = added_face(encode_face_list)


