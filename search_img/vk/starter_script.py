import get_data_vk
import os
import csv


def start(id_vk):
    '''
    id_vk - айди пользователя
    ID_DIR - имя папки
    PATH_DISK - путь где лежат данные
    PATH_SCRIPT - путь для создание csv


    '''
    PATH_SCRIPT = PATH_DISK + str(id_vk)

    def create_dir():
        '''
        создает папку где хранятся фотки
        создает csv где хранятся данные
        '''
        def fiiling_cap_data():
            with open(f'{PATH_SCRIPT}/data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                #writer.writerow(['id', 'profile_link', 'photo_link', 'encode'])

        if not os.path.exists(PATH_SCRIPT):
            os.mkdir(PATH_SCRIPT)
        fiiling_cap_data()
        if not os.path.exists(f'{PATH_SCRIPT}/vk_photo'):
            os.mkdir(f'{PATH_SCRIPT}/vk_photo')

    def main(id_vk):
        '''
        id_vk - айди пользователя

        заполняет csv данными
        '''
        get_data_vk.get_photo_vk(id_vk=id_vk, PATH_DISK=PATH_SCRIPT)

    create_dir()
    main(id_vk)


if __name__ == '__main__':
    PATH_DISK = '/home/daniil1/learn/deanoner_bd/bd_vk/'
    start(id_vk=294361315)


