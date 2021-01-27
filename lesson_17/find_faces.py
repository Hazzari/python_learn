import sys
from random import random, randint

from icecream import ic

import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE = "image-1.jpeg"

faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)


def main():
    # Читаем картинку
    img = cv2.imread(IMAGE)
    # ic(img)
    # ic(img.shape)

    # opencv ищет по серой картинке по этому конвертируем в серый
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ic(img_gray)
    # ic(img_gray.shape)

    # Ищем лица на картинке
    faces = faces_cascade_db.detectMultiScale(img_gray)
    print(faces.shape)  # считаем количество найденных лиц

    # x, y верхние левые координаты
    # w, h ширина и высота картинки
    for i, (x, y, w, h) in enumerate(faces):
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        # Пытаемся сделать разные цвета найденных лиц
        B = (i * 10 + int(x) ** i) % 255
        G = (i * 25 + int(x) ** i) % 255
        cv2.rectangle(img, pt1, pt2, color=(B, G, 255), thickness=2)

    cv2.imshow("Image", img)
    while True:
        key = cv2.waitKey(0)
        if key and key == ord("q"):
            print('Exit key', key)
            break

    cv2.destroyWindow('Image')


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
    sys.exit(0)
