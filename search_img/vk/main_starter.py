import threading
import starter_script
import time



ID_VK = 1
NUM_DIR = 1 #const
NUM_OF_SCRIPTS = 10000

num_dir = NUM_DIR
id_vk = ID_VK


for el in range(NUM_OF_SCRIPTS):
    t = threading.Thread(target=starter_script.start, name='Script', args=(id_vk, num_dir))
    t.start()
    id_vk += 1
    num_dir += NUM_DIR
    time.sleep(5)
