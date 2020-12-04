import requests

TOKEN = "177de17765ea954d1c9ab6cead9613d8298f009ad40cfb7d4203377888be931eba08706a3311fc0919bbc"
FILENAME = 1
'''
TOKEN - необходим для авторизации в вк через vk_api
FILENAME - используется для названий фотографий
'''

def parser_profile_api(id_vk,PATH_DISK):
    '''
    id_vk - айди пользователя в вк
    PATH_DISK - путь к папке где будут записываться данные пользователя
    result_dic - result_dic{'имя фотки': 'ссылка на фотку'}

    return список result_dic{'имя фотки': 'ссылка на фотку'}
    '''
    result_dic = {}
    def file_name():
        '''
        увеличивает название для фотографии на 1
        '''
        global FILENAME
        FILENAME += 1

    def count_offset(id_album,id_vk):
        '''
        id_album - айди альбома у пользователя
        id_vk - айди пользователя

        возвращает список ссылок на фотографий
        '''
        id = id_album
        r = requests.get('https://api.vk.com/method/photos.get', params={'owner_id': id_vk,
                                                                         'access_token': TOKEN,
                                                                         'photo_sizes': 1,
                                                                         'v': 5.89,
                                                                         'album_id': id,
                                                                         'count': 50
                                                                         })

        return int(r.json()['response']['count'])

    def get_largest(size_list):
        '''
        size_list - список 1 одной фотографий разных размеров
        LIST_SIZE - список возможный размеров в вк

        возрващает фотографию наибольшего размера
        '''
        LIST_SIZE = ['s', 'm', 'x', 'y', 'z', 'w']
        count = -1
        while True:
            for el_size in size_list:
                if el_size['type'] == LIST_SIZE[count]:
                    return el_size['url'] #return url largest photo
                else:
                    continue
            count -= 1

    # пытался сделать проверку если сервер ответил не 200, в результате стало хуже, возможно из за того, что криво написал
    def download_photo(url, date_photo):
        '''
        url - ссылка на фотку
        PATH_DISK - путь к папке где будут записываться данные пользователя
        FILENAME - имя фотографии

        закачивают фотку на диск и переименновывает ее
        записывает в result_dic{'имя фотки': 'ссылка на фотку'}
        '''
        r = requests.get(url)
        name_photo = f'{PATH_DISK}/vk_photo/{FILENAME}.jpg'
        with open(name_photo, 'wb') as file:
            result_dic[name_photo] = {'url': url, 'date_photo': date_photo}
            file.write(r.content)

    def take_photo(el_album_id, COUNT, offset, id_vk):
        '''
        el_album_id - айди альбома
        COUNT - положительное число, по умолчанию 50 , максимальное значение 1000, количество скачинных фоток
        offset - с какого номера фотки начинать дальше качать
        id_vk - айди пользователя в вк

        получает самое большое изображение, скачивает его на диск и увеличивает имя следующей фотки на 1
        '''
        r = requests.get('https://api.vk.com/method/photos.get', params={'owner_id': id_vk,
                                                                         'access_token': TOKEN,
                                                                         'photo_sizes': 1,
                                                                         'v': 5.89,
                                                                         'album_id': el_album_id,
                                                                         'count': COUNT,
                                                                         'offset': offset
                                                                             })

        photos = r.json()['response']['items']
        for photo in photos:
            sizes = photo['sizes']
            date_photo = photo['date']
            max_size_url = get_largest(sizes)
            download_photo(url=max_size_url, date_photo=date_photo)
            file_name()
            #print(max_size_url) #выводит в консоль изображение

    def main(id_vk):
        '''
        id_vk - айди пользователя в вк
        COUNT - положительное число, по умолчанию 50 , максимальное значение 1000, количество скачинных фоток
        offset - с какого номера фотки начинать дальше качать
        album_id_list - список айди альбомов пользователя

        получает список альбомов пользователей.
        получает список фотографий пользователей и закачивает их в папку.
        '''
        COUNT = 1000
        album_id_list = take_album_id(id_vk=id_vk)
        for el_album_id in album_id_list:
            max_offset = count_offset(el_album_id, id_vk=id_vk)
            offset = 0
            while offset < max_offset:
                take_photo(el_album_id=el_album_id, COUNT=COUNT, offset=offset, id_vk=id_vk)
                offset += COUNT


    def take_album_id(id_vk):
        '''
        id_vk - айди пользователя в вк
        album_id_list - список айди альбомов пользователя

        return список айди альбомов пользователя
        '''
        album_id_list = []
        r = requests.get('https://api.vk.com/method/photos.getAlbums', params={'owner_id': id_vk,
                                                                               'access_token': TOKEN,
                                                                               'need_system': 1,
                                                                               'v': 5.89
                                                                               })

        content = r.json()['response']['items']
        for el_album_id in content:
            album_id_list.append(el_album_id['id'])
        return album_id_list

    main(id_vk)
    return result_dic

