from get_user_media import get_user_media
from encoding_face import main_encoding_face
from get_profile_name import get_profile_name
import get_secondary_data
import shutil,os
import csv

def get_profile_BD(ID, PATH):

    PATH_PROFILE = PATH + str(ID)

    def write_data(list_link_and_encoding, profile_link, data_profile):
        '''
        list_link_and_encoding - список ссылок на фотку и список массивов на фотку
        profile_link - ссылка на пользователя
        data_profile - данные профиля
        записывает в csv данные
        '''

        def registration(profile_link='unknown',
                         photo_link='unknown',
                         encode='unknown',
                         preview_photo='unknown',
                         preview_face='unknown',
                         date_photo='unknown',
                         sex='unknown',
                         city='unknown',
                         bdate='unknown',
                         name='unknown'
                         ):
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([profile_link,
                             photo_link,
                             encode,
                             preview_photo,
                             preview_face,
                             date_photo,
                             sex,
                             city,
                             bdate,
                             name
                             ])

        with open(f'{PATH_PROFILE}/data.csv', 'a', newline='') as csvfile:
            for link_and_encode in list_link_and_encoding.items():
                for el_encode, preview_face in zip(link_and_encode[1]['data']['encode'],
                                                   link_and_encode[1]['data']['preview_face_list']):
                    registration(profile_link=profile_link,
                                 photo_link=link_and_encode[0],
                                 encode=el_encode,
                                 preview_photo=link_and_encode[1]['data']['preview_photo'],
                                 preview_face=preview_face,
                                 date_photo=link_and_encode[1]['date_photo'],
                                 #sex=data_profile['sex'],
                                 #city=data_profile['city'],
                                 #bdate=data_profile['bdate'],
                                 name=data_profile['name']
                                 )


    def remove_folder_contents(path):
        path = path + '/photo'
        '''
        очищает папку где лежат фотографии
        '''
        shutil.rmtree(path)
        os.makedirs(path)

    def swap(namePhoto_and_linkPhoto, namePhoto_and_encodingPhoto):
        '''
        namePhoto_and_linkPhoto - список ссылок на фотки
        namePhoto_and_encodingPhoto - список массивов всех фоток
        делает новый словарь - {'ссылка на фотку': 'массив фотки'}
        return возвращает новый словарь
        '''

        res_list = {}
        for el in namePhoto_and_encodingPhoto:
            res_list[namePhoto_and_linkPhoto[el]['url']] = {'data': namePhoto_and_encodingPhoto[el],
                                                            'date_photo': namePhoto_and_linkPhoto[el]['date_photo']
                                                            }
        return res_list

    '''
    id_vk - айди пользователя в вк
    namePhoto_and_linkPhoto - список result_dic{'имя фотки': 'ссылка на фотку'}
    '''

    def main(ID):
        try:
            login = get_profile_name(ID)
            name = login['name']
            profile_link = 'https://www.instagram.com/' + name
            print(name)
            namePhoto_and_linkPhoto = get_user_media(name_acc=name, path=PATH_PROFILE, ID=ID)
            namePhoto_and_encodingPhoto = main_encoding_face(PATH_PROFILE=PATH_PROFILE)
            remove_folder_contents(PATH_PROFILE)
            list_link_and_encoding = swap(namePhoto_and_linkPhoto, namePhoto_and_encodingPhoto)
            data_profile = get_secondary_data.get_data(profile_link=profile_link)
            write_data(list_link_and_encoding=list_link_and_encoding, profile_link=profile_link, data_profile=data_profile)
        except KeyError:  # ошибка возникает если у человека закрытый профиль
            remove_folder_contents(PATH_PROFILE)
            return

    main(ID)

if __name__ == '__main__':
    ID = 5461737491
    PATH = '/home/daniil1/learn/deanoner_bd/bd_inst/'
    get_profile_BD(ID=ID, PATH=PATH)