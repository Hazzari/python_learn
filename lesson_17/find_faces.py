import sys

import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE = "image-1.jpeg"


def main():
    img = cv2.imread(IMAGE)

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
