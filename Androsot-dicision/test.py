# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import math


def video_preparation(frame):
    hue_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_range = np.array([26, 43, 46])
    high_range = np.array([34, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)
    gaus = cv2.GaussianBlur(th, (7, 7), 1.5)

    eroded = cv2.erode(gaus, cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (4, 4)), iterations=2)

    dilated = cv2.dilate(eroded, cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)

    contours, hierarchy = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(dilated, contours, -1, (0, 0, 255), 10)
    return contours, dilated


def ball_detection(contours):
    loca = []
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area > 280:
            return [x, y, w, h, area]


def main():
    path = "2022-01-06_19-22-24.mp4"
    # path = 0
    cap = cv2.VideoCapture(path)
    if cap.isOpened() is True:
        while(True):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            contours, frame = video_preparation(frame)
            loca = ball_detection(contours)
            if loca != None:
                print((loca[0] + loca[2])/2, (loca[1] + loca[3])/2)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print('ball is not opened!')


if __name__ == '__main__':
    main()
