import csv, shutil, os
import dowload_vk_profile_photo, encoding_face, get_secondary_data

'''
URl - ссылка на список всех пользователей в вк
HOST - используется для конкатенацией с id_vk чтобы получить ссылку на профиль
ID - служат для название картинок, чтобы у картинок не совпадали именна
'''

URL = 'https://vk.com/catalog.php'
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106 (Edition Yx)'}
HOST = 'https://vk.com/id'


def get_photo_vk(id_vk, PATH_DISK):
    '''
    id_vk - айди пользователя в вк
    PATH_DISK - путь к папке где будут записываться данные пользователя
    '''

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

        with open(f'{PATH_DISK}/data.csv', 'a', newline='') as csvfile:
            for link_and_encode in list_link_and_encoding.items():
                for el_encode, preview_face in zip(link_and_encode[1]['data']['encode'],
                                                   link_and_encode[1]['data']['preview_face_list']):
                    registration(profile_link=profile_link,
                                 photo_link=link_and_encode[0],
                                 encode=el_encode,
                                 preview_photo=link_and_encode[1]['data']['preview_photo'],
                                 preview_face=preview_face,
                                 date_photo=link_and_encode[1]['date_photo'],
                                 sex=data_profile['sex'],
                                 city=data_profile['city'],
                                 bdate=data_profile['bdate'],
                                 name=data_profile['name']
                                 )

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

    def remove_folder_contents(path=f'{PATH_DISK}/vk_photo'):
        '''
        очищает папку где лежат фотографии
        '''
        shutil.rmtree(path)
        os.makedirs(path)

    def main(id_vk):
        '''
        id_vk - айди пользователя в вк
        namePhoto_and_linkPhoto - список result_dic{'имя фотки': 'ссылка на фотку'}
        '''
        try:
            profile_link = HOST + str(id_vk)
            #print(profile_link)
            namePhoto_and_linkPhoto = dowload_vk_profile_photo.parser_profile_api(id_vk, PATH_DISK=PATH_DISK)
            namePhoto_and_encodingPhoto = encoding_face.main_encoding_face(PATH_DISK=PATH_DISK)
            remove_folder_contents()
            list_link_and_encoding = swap(namePhoto_and_linkPhoto=namePhoto_and_linkPhoto, namePhoto_and_encodingPhoto=namePhoto_and_encodingPhoto)
            data_profile = get_secondary_data.get_secondary_data(id_vk)
            write_data(list_link_and_encoding=list_link_and_encoding, profile_link=profile_link, data_profile=data_profile)
            print()
        except KeyError:  # ошибка возникает если у человека закрытый профиль
            remove_folder_contents()
            return

    main(id_vk)

if __name__ == '__main__':
    get_photo_vk(id_vk=1, PATH_DISK='C:/vk_check')