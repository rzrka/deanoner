import requests
import csv, shutil, os, sys, time
from bs4 import BeautifulSoup
import dowload_vk_profile_photo, encoding_face

URL = 'https://vk.com/catalog.php'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106 (Edition Yx)'}
HOST = 'https://vk.com/id'
ID = 1
PATH_DISK = 'C:/vk_test/'


def parsing_profile(id_vk):

    def write_data(list_link_and_encoding, profile_link):
        global ID
        with open(f'{PATH_DISK}data.csv', 'a', newline='') as csvfile:
            for link_and_encode in list_link_and_encoding.items():
                for el_encode in link_and_encode[1]:
                    writer = csv.writer(csvfile, delimiter=';')
                    writer.writerow([ID, profile_link, link_and_encode[0], el_encode])
                    ID += 1

    def swap(list_link, list_encode):
        res_list = {}
        for el in list_encode:
            res_list[list_link[el]] = list_encode[el]
        return res_list

    def remove_folder_contents(path=f'{PATH_DISK}vk_photo'):
        shutil.rmtree(path)
        os.makedirs(path)

    def main(id_vk):
        try:
            profile_link = HOST + str(id_vk)
            namePhoto_and_linkPhoto = dowload_vk_profile_photo.parser_profile_api(id_vk, PATH_DISK=PATH_DISK)
            namePhoto_and_encodingPhoto = encoding_face.main_encoding_face(profile_link, PATH_DISK=PATH_DISK)
            remove_folder_contents()
            list_link_and_encoding = swap(namePhoto_and_linkPhoto, namePhoto_and_encodingPhoto)
            write_data(list_link_and_encoding, profile_link=profile_link)
            sys.exit()  # test
        except KeyError:# ошибка возникает если у человека закрытый профиль или не кликабельная ава. Надо запускать обработку через парсинг странички
            remove_folder_contents()
            return


    main(id_vk)
parsing_profile(63)