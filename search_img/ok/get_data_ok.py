import download_ok_profile_photo, encoding_face, get_secondary_data
import os, csv

#HOST = 'https://ok.ru/profile/'

#PATH_DISK = PATH + user_id
def get_data_ok(user_id, PATH):
    HOST = 'https://ok.ru/profile/'

    PATH_DISK = PATH + str(user_id)
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
                                 #date_photo=link_and_encode[1]['date_photo'],
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

    def main(user_id):
        user_id = str(user_id)
        try:
            os.mkdir(PATH_DISK)
        except OSError:
            pass
        try:
            profile_link = HOST + str(user_id)
            namePhoto_and_linkPhoto = download_ok_profile_photo.main_photo(user_id=user_id,PATH_DISK=PATH_DISK)
            namePhoto_and_encodingPhoto = encoding_face.main_encoding_face(PATH_PROFILE=PATH_DISK)
            list_link_and_encoding = swap(namePhoto_and_linkPhoto=namePhoto_and_linkPhoto,
                                          namePhoto_and_encodingPhoto=namePhoto_and_encodingPhoto)
            data_profile = get_secondary_data.get_secondary_data(user_id=user_id)
            write_data(list_link_and_encoding=list_link_and_encoding, profile_link=profile_link, data_profile=data_profile)
        except:
            pass
    main(user_id=user_id)
if __name__ == '__main__':
    get_data_ok(user_id=347465666795,
                PATH='/home/daniil1/learn/deanoner_bd/bd_ok/')