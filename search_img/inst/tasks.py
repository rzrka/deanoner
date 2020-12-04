import cv2
import numpy as np

def check1():
    image_same1 = cv2.imread(img1)
    image_same2 = cv2.imread(img2)
    img = cv2.imread(img3)


    image_same1_by = cv2.imencode('.jpg', image_same1)[1].tostring()
    image_same2_by = cv2.imencode('.jpg', image_same2)[1].tostring()
    img_by = cv2.imencode('.jpg', img)[1].tostring()


    nparr1 = np.fromstring(image_same1_by, np.uint8)
    nparr2 = np.fromstring(image_same2_by, np.uint8)
    nparr3 = np.fromstring(img_by, np.uint8)
    image_same1 =cv2.imdecode(nparr1, cv2.IMREAD_COLOR)
    image_same2 =cv2.imdecode(nparr2, cv2.IMREAD_COLOR)
    img = cv2.imdecode(nparr3, cv2.IMREAD_COLOR)

    if image_same1_by == image_same2_by:
        print(len(image_same1_by))
        print(len(image_same2_by))
        cv2.imshow('image_same1_by', image_same1)
        cv2.waitKey(0)
        cv2.imshow('image_same2_by', image_same2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if img_by != image_same1_by:
        print(len(img_by))
        print(len(image_same1_by))
        cv2.imshow('image_same1_by', image_same1)
        cv2.waitKey(0)
        cv2.imshow('img_by', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


img1 = "C:/vk_test/test/check1.dll"
img2 = "C:/vk_test/test/check2.dll"
img3 = "C:/vk_test/test/img.dll"

check1()

