import requests
import hashlib
from collections import OrderedDict
import os
from datetime import timezone,datetime

access_token = 'tkn1kMqV5GKxu2VL0SZZ8U4f5MTcppLpEirkvaRfpYBvoKKRNL1i6Md5VWjHPTdIFcI5i'
secret_session_key = '46e5b852d4cfa46f16288294a3ab839c'
application_key = 'CINLNMJGDIHBABABA'
application_id = '512000514775'
user_id = '522122120601'
URL = 'https://api.ok.ru/fb.do'
def generate_sig(var):
    var = OrderedDict(sorted(var.items()))
    sig = ''
    for el in var.items():
        sig += el[0] + '='
        sig += el[1]
    sig += secret_session_key
    hash_object = hashlib.md5(sig.encode('utf-8'))
    return hash_object.hexdigest()

def get_secondary_data(user_id):
    variables = {'application_key': 'CINLNMJGDIHBABABA',
                 'fields': 'BIRTHDAY,NAME,GENDER,LOCATION',
                 'format': 'json',
                 'method': 'users.getInfo',
                 'uids': user_id
                 }
    result = {}
    r = requests.get(URL, params={'application_key': variables['application_key'],
                                  'fields': variables['fields'],
                                  'format': variables['format'],
                                  'method': variables['method'],
                                  'uids': variables['uids'],
                                  'sig': generate_sig(variables),
                                  'access_token': 'tkn1EnfeXJiNAWLek7o3yriCvsFk1LvVv5da87zxF7lL0cJmfNsuExKtkZqgdUOOIcv4Z1'
                                  })
    info = r.json()[0]

    def get_bdate():
        try:
            if len(info['birthday']) > 7:
                dt = datetime.strptime(info['birthday'],'%Y-%m-%d')
                unix2 = int(dt.replace(tzinfo=timezone.utc).timestamp())
                result['bdate'] = unix2
            result['bdate'] = 'unknown'
        except KeyError:
            result['bdate'] = 'unknown'
            return

    def get_sex():
        try:
            if info['gender'] == '':
                raise KeyError
            result['sex'] = info['gender']
        except KeyError:
            result['sex'] = 'unknown'
            return

    def get_city():
        try:
            if info['location']['city'] == '':
                raise KeyError
            result['city'] = info['location']['city']
        except KeyError:
            result['city'] = 'unknown'
            return
    def get_name():
        try:
            if info['name'] == '':
                raise KeyError
            result['name'] = info['name']
        except KeyError:
            result['name'] = 'unknown'

    get_name()
    get_bdate()
    get_sex()
    get_city()

    return result

if __name__ == '__main__':
    PATH_DISK = 'C:/ok_test/522122120601'
    get_secondary_data(user_id=user_id)