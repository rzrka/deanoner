import os
import requests
import urllib.request

FILENAME = 1
# download images
def get_user_media(name_acc, path, ID):

    result_dic = {}

    def image_downloader(edge, images_path):
        global FILENAME
        display_url = edge['node']['display_url']
        date_photo = edge['node']['taken_at_timestamp']

        download_path = images_path + '/' + str(FILENAME) + '.jpg'
        urllib.request.urlretrieve(display_url, download_path)
        result_dic[download_path] = {'url': display_url,
                                     'date_photo':date_photo
                                     }
        FILENAME += 1
        print(download_path)




    # download images and videos from posts containing more than one pictures or videos`
    def sidecar_downloader(shortcode, images_path):
        global FILENAME
        r = requests.get('https://www.instagram.com/p/' + shortcode + '/?__a=1')
        for edge in r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
            is_video = edge['node']['is_video']
            if is_video == False:
                display_url = edge['node']['display_url']
                try:
                    date_photo = edge['node']['taken_at_timestamp']
                except KeyError:
                    date_photo = 'unknown'
                download_path = images_path + '/' + str(FILENAME) + '.jpg'
                urllib.request.urlretrieve(display_url, download_path)
                result_dic[download_path] = {'url': display_url,
                                             'date_photo': date_photo
                                             }
                FILENAME += 1
                print(download_path)
            else:
                continue

    def main(account_json_info, path):
        r = requests.get(account_json_info)
        user_id = r.json()['graphql']['user']['id']
        end_cursor = ''
        next_page = True
        images_path = path + '/photo'
        try:
            os.makedirs(path + '/photo')
        except FileExistsError:
            pass

        while next_page == True:
            r = requests.get('https://www.instagram.com/graphql/query/',
                    params = {
                        'query_id': '17880160963012870',
                        'id': user_id,
                        'first': 12,
                        'after': end_cursor
                    }
            )
            graphql = r.json()['data']
            for edge in graphql['user']['edge_owner_to_timeline_media']['edges']:
                __typename = edge['node']['__typename']
                if __typename == 'GraphImage':
                    image_downloader(edge, images_path)
                elif __typename == 'GraphSidecar':
                    shortcode = edge['node']['shortcode']
                    sidecar_downloader(shortcode, images_path)

            end_cursor = graphql['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            next_page = graphql['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']

    account_json_info = 'https://www.instagram.com/' + name_acc + '/?__a=1'  # insert username into the link
    main(account_json_info, path)
    return result_dic

if __name__ == '__main__':
    name_acc = 'rzrka5555'
    path = 'C:/inst_test'
    get_user_media(name_acc, path, 1)