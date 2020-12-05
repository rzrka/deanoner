import cv2, os
import numpy as np
import face_recognition
from mtcnn import MTCNN
import adding_faces

def detected_fc(image):
        #fac_loc = face_recognition.face_locations(image)[0]
        fac_encode = face_recognition.face_encodings(image)
        return fac_encode

image_main = cv2.cvtColor(cv2.imread('../test_img2/main.jpg'), cv2.COLOR_BGR2RGB)
encode_main = detected_fc(image_main)[0]
#encode_main = adding_faces.result_adding_face
none_detec_list = []
res_list = [] #список всех лиц
#перебор всех фалов из папки
path = '../test_img2/'
image_paths = [os.path.join(path, f) for f in os.listdir(path)]
for el_image in image_paths:
    try:
        if el_image.endswith('.jpg') or el_image.endswith('.jpeg'):
            image_check_fc = cv2.cvtColor(cv2.imread(el_image), cv2.COLOR_BGR2RGB)
            encode_check_fc = detected_fc(image_check_fc)

            for encode_check_el in encode_check_fc:
                results = face_recognition.compare_faces([encode_main], encode_check_el, tolerance=0.6)
                #face_dis = face_recognition.face_distance([encode_main], encode_check_fc)
                if results[0]:
                    res_list.append(el_image)
    except IndexError:
        none_detec_list.append(el_image)
        continue


print(res_list)
print(len(res_list))
print(none_detec_list)
print(len(none_detec_list))