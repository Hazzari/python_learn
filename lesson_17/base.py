import sys
import cv2

EXIT_KEY = 27  # Escape


def main(cap):
    while True:
        success, img = cap.read()
        if not success:
            print("Cloud not read frame!")
            break

        cv2.imshow("Select", img)
        key = cv2.waitKey(5)
        if key == EXIT_KEY:
            break

    # Закрываем окно
    cv2.destroyWindow("Select")


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    try:
        main(cap)
    finally:
        cap.release()
    sys.exit(0)
