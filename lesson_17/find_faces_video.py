import sys
import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE = "image-1.jpeg"

EXIT_KEY = 27  # Escape
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)


def main(capture: cv2.VideoCapture):
    frame_count = 0
    faces = []
    while True:
        # Читаем изображение с камеры
        success, img = cap.read()
        if not success:
            print('Could not frame!')
            break

        if frame_count % 10 == 0:
            faces = faces_cascade_db.detectMultiScale(img)

        frame_count += 1

        # x, y верхние левые координаты
        # w, h ширина и высота картинки
        for x, y, w, h in faces:
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            # Пытаемся сделать разные цвета найденных лиц
            cv2.rectangle(img, pt1, pt2, color=(0, 0, 255), thickness=2)

        # Показываем окно
        cv2.imshow('Video', img)

        # Отмена окна по ключу
        key = cv2.waitKey(1)

        if key == EXIT_KEY:
            print('exit by key')
            break

    # Закрываем окно
    cv2.destroyWindow('Video')


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    try:
        main(cap)
    finally:
        cap.release()
    sys.exit(0)
