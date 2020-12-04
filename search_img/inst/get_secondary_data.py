import requests

def get_data(profile_link):
    account_json_info = profile_link + '/?__a=1'
    result = {}
    r = requests.get(account_json_info)
    def get_name():
        name = r.json()['graphql']['user']['full_name']
        try:
            if not name == '':
                result['name'] = name
            else:
                raise KeyError
        except KeyError:
            result['name'] = 'unknown'

    get_name()
    return result

if __name__ == '__main__':
    name = 'rzrka5555'
    profile_link = 'https://www.instagram.com/' + name
    get_data(profile_link)