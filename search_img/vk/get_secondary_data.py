import requests
TOKEN = "177de17765ea954d1c9ab6cead9613d8298f009ad40cfb7d4203377888be931eba08706a3311fc0919bbc"

def get_secondary_data(id_vk):
    '''
    id_vk - айди пользователя
    result - словарь {'city': 'город', 'sex': 'пол' 'bdate': 'дата рождения'}

    return словарь result
    '''
    result = {}

    r = requests.get('https://api.vk.com/method/users.get', params={'user_id': id_vk,
                                                                    'access_token': TOKEN,
                                                                    'fields': 'bdate, sex, city',
                                                                    'v': 5.89,
                                                                    })
    r = r.json()['response'][0]
    def get_sex():
        try:
            if r['sex'] == 2:
                result['sex'] = 'male'
            elif r['sex'] == 1:
                result['sex'] = 'female'
        except KeyError:
            result['sex'] = 'unknown'
            return

    def get_city():
        try:
            result['city'] = r['city']['title']
        except KeyError:
            result['city'] = 'unknown'
            return

    def get_bdate():
        try:
            if len(r['bdate']) > 7:
                result['bdate'] = r['bdate']
            result['bdate'] = 'unknown'
        except KeyError:
            result['bdate'] = 'unknown'
            return
    def get_name():
        try:
            name =f'{r["first_name"]} {r["last_name"]}'
            result['name'] = name
        except KeyError:
            result['name'] = 'unknown'

    get_name()
    get_sex()
    get_city()
    get_bdate()

    return result
