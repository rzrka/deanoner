import requests
import hashlib
from collections import OrderedDict
import os

access_token = 'tkn1kMqV5GKxu2VL0SZZ8U4f5MTcppLpEirkvaRfpYBvoKKRNL1i6Md5VWjHPTdIFcI5i'
secret_session_key = '46e5b852d4cfa46f16288294a3ab839c'
application_key = 'CINLNMJGDIHBABABA'
application_id = '512000514775'
user_id = '522122120601'
URL = 'https://api.ok.ru/fb.do'
FILENAME = 1

def generate_sig(var):
    var = OrderedDict(sorted(var.items()))
    sig = ''
    for el in var.items():
        sig += el[0] + '='
        sig += el[1]
    sig += secret_session_key
    hash_object = hashlib.md5(sig.encode('utf-8'))
    return hash_object.hexdigest()

def get_date_photo():
    return 'unknown'

def get_album(user_id):
    variables = {'application_key': 'CINLNMJGDIHBABABA',
                 'fid': user_id,
                 'format': 'json',
                 'method': 'photos.getAlbums'
                 }
    album_list = []
    r = requests.get(URL, params={'application_key': variables['application_key'],
                                  'fid': variables['fid'],
                                  'format': variables['format'],
                                  'method': variables['method'],
                                  'sig': generate_sig(variables),
                                  'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                  })
    albums = r.json()['albums']
    for album in albums:
        album_list.append(album['aid'])
    return album_list


def get_photo(user_id, album_id=None):
    variables = {'application_key': 'CINLNMJGDIHBABABA',
                 'count':'100',
                 'fid': user_id,
                 'fields': 'photo.pic_max',
                 'format': 'json',
                 'method': 'photos.getPhotos'
                 }
    url_photo = []
    if album_id == None:
        r = requests.get(URL, params={'application_key': variables['application_key'],
                                      'count': variables['count'],
                                      'fid': user_id,
                                      'fields': variables['fields'],
                                      'format': variables['format'],
                                      'method': variables['method'],
                                      'sig': generate_sig(variables),
                                      'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                      })
        photos = r.json()['photos']
        for photo in photos:
            url_photo.append({'url': photo['pic_max'], 'date': 'unknown'})
        has_more = r.json()['hasMore']
        while has_more:
            anchor = r.json()['anchor']
            variables['anchor'] = anchor
            r = requests.get(URL, params={'anchor': variables['anchor'],
                                          'application_key': variables['application_key'],
                                          'count': variables['count'],
                                          'fid': user_id,
                                          'fields': variables['fields'],
                                          'format': variables['format'],
                                          'method': variables['method'],
                                          'sig': generate_sig(variables),
                                          'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                          })
            photos = r.json()['photos']
            for photo in photos:
                url_photo.append({'url': photo['pic_max'], 'date': 'unknown'})
            has_more = r.json()['hasMore']
        if 'anchor' in variables.keys():
            del variables['anchor']
        return url_photo
    if album_id != None:
        variables['aid'] = album_id
        r = requests.get(URL, params={'aid': variables['aid'],
                                      'application_key': variables['application_key'],
                                      'count': variables['count'],
                                      'fid': user_id,
                                      'fields': variables['fields'],
                                      'format': variables['format'],
                                      'method': variables['method'],
                                      'sig': generate_sig(variables),
                                      'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                      })
        photos = r.json()['photos']
        for photo in photos:
            url_photo.append({'url': photo['pic_max'], 'date': 'unknown'})
        has_more = r.json()['hasMore']
        while has_more:
            anchor = r.json()['anchor']
            variables['anchor'] = anchor
            r = requests.get(URL, params={'aid': variables['aid'],
                                          'anchor': variables['anchor'],
                                          'application_key': variables['application_key'],
                                          'count': variables['count'],
                                          'fid': user_id,
                                          'fields': variables['fields'],
                                          'format': variables['format'],
                                          'method': variables['method'],
                                          'sig': generate_sig(variables),
                                          'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                          })
            photos = r.json()['photos']
            for photo in photos:
                url_photo.append({'url': photo['pic_max'], 'date': 'unknown'})
            has_more = r.json()['hasMore']
        if 'anchor' in variables.keys():
            del variables['anchor']
        return url_photo

def download_photo(photos,PATH_DISK):
    result_dic = {}
    global FILENAME
    for photo in photos:
        r = requests.get(photo['url'])
        name_photo = f'{PATH_DISK}/photo/{FILENAME}.jpg'
        with open(name_photo, 'wb') as file:
            result_dic[name_photo] = {'url': photo['url'], 'date_photo': photo['date']}
            file.write(r.content)
        FILENAME += 1
    return result_dic

def main_photo(user_id, PATH_DISK):
    photos = []

    try:
        os.mkdir(PATH_DISK+'/photo')
    except OSError:
        pass

    albums = get_album(user_id)
    for el in get_photo(user_id=user_id):
        photos.append(el)
    for album in albums:
        for el in (get_photo(user_id=user_id,album_id=album)):
            photos.append(el)
    return download_photo(photos,PATH_DISK=PATH_DISK)

if __name__ == '__main__':
    PATH_DISK = 'C:/ok_test/522122120601'
    main_photo(user_id=user_id,PATH_DISK=PATH_DISK)



