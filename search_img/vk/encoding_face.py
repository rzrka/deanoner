import cv2
import face_recognition
import os

def main_encoding_face(PATH_DISK):
    '''
    PATH_DISK - путь где лежат фотографии
    path - путь где лежат фотографии
    image_paths - список всех ссылок фотографиий
    image_name - имя фотоки
    resilt_dic - список {'имя фото': 'массив фото'}

    определяет массив лица и записывает в result_dic имя фотки и его массив

    return список {'имя фото': 'массив фото'}
    '''
    result_dic = {}

    def get_preview_face_list(image):
        face_list = []
        fac_loc = face_recognition.face_locations(image)
        for el_face in fac_loc:
            cropped = image[el_face[0]:el_face[2], el_face[3]:el_face[1]]
            cropped = cv2.resize(cropped, (200, 200), interpolation=cv2.INTER_AREA)
            img_to_byte = cv2.imencode('.jpg', cropped)[1].tostring()
            face_list.append(img_to_byte)
        return face_list

    def get_preview_photo(image):
        image = cv2.resize(image, (200, 200), interpolation=cv2.INTER_AREA)
        img_to_byte = cv2.imencode('.jpg', image)[1].tostring()
        return img_to_byte

    def get_encode_image(image):
        image_encode = face_recognition.face_encodings(image)
        return image_encode

    # перебор всех файлов из папки
    path = f'{PATH_DISK}/vk_photo/'
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    for image in image_paths:
        if image.endswith('.jpg') or image.endswith('.jpeg'):
            try:  # загрузилась сшиком большая фотография
                image_name = image
                image = cv2.cvtColor(face_recognition.load_image_file(f'{image_name}'), cv2.COLOR_BGR2RGB)
                encode_image = get_encode_image(image)
                if encode_image != []:
                    preview_photo = get_preview_photo(image)
                    preview_face_list = get_preview_face_list(image)
                    result_dic[image_name] = {'encode': encode_image,
                                              'preview_photo': preview_photo,
                                              'preview_face_list': preview_face_list
                                              }
            except:
                continue

                # print(f'{image_name} добавилось') #тест
        else:
            continue
    #with open('C:/vk_test/result.txt', 'w') as f:
        #f.write(str(result_dic))
    return result_dic


if __name__ == '__main__':
    print(main_encoding_face('C:/vk_test/1'))


