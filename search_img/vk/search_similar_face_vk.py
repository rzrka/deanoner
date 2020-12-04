import face_recognition, cv2
import numpy as np
import csv
import sys


PATH_DISK = 'C:/vk_test/'
main_path = f'{PATH_DISK}result.csv'
def detected_fc(image_path):
    # fac_loc = face_recognition.face_locations(image)[0]
    image = cv2.cvtColor(face_recognition.load_image_file(f'{image_path}'), cv2.COLOR_BGR2RGB)
    image_encode = face_recognition.face_encodings(image)
    return image_encode

def from_string_to_numpy(image):
    image = image[1:-1].split()
    image = np.array(image)
    image = image.astype(np.float)
    return image

def count_photo(profile_link,reader):
    count = 0
    with open(main_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if profile_link == row['profile_link']:
                count += 1
    return count


image_input = detected_fc(f'{PATH_DISK}input_img/check.jpg')[0]

result_dic = {}
my_count = 0
with open(main_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        data_encode = from_string_to_numpy(row['encode'])
        data_profile_link = row['profile_link']
        data_photo_link = row['photo_link']
        result = face_recognition.compare_faces([image_input], data_encode)[0]
        if result == True:
            print(count_photo(data_profile_link, reader))
            if data_profile_link not in result_dic:
                result_dic[data_profile_link] = {'count': 0, 'photo_link': []}
            result_dic[data_profile_link]['photo_link'].append(data_photo_link)
            result_dic[data_profile_link]['count'] += 1

    result_dic = sorted(result_dic.items(), key=lambda x: x[1]['count'], reverse=True)
    print(result_dic)





