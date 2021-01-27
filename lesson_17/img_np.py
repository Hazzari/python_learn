# Пример того как картинка отрисовывается через np

import sys

import cv2
import numpy as np

SHAPE = 480, 640, 3


def main():
    img = np.zeros(SHAPE, np.uint8)
    # img[..., [0, 1]] = 255
    img[..., 0] = 90
    img[..., 1] = 196
    img[..., 2] = 255
    # img[...] = 255  # Меняем цвет картинки

    print(img)
    print(img.shape)

    cv2.imshow("Image", img)

    while True:
        key = cv2.waitKey(0)
        if key and key == ord("q"):
            print('Exit key', key)
            break

    cv2.destroyWindow('Image')
    sys.exit(0)


if __name__ == '__main__':
    main()
