from PIL import ImageGrab
import numpy as np
import cv2
import serial
import time

word_list_num = 5

counter = 0
ser = serial.Serial('com5', 9600)

while True:

    img = np.array(ImageGrab.grab(bbox=(1, 329, 610, 1390)))
    # img = np.array(ImageGrab.grab())
    cv2.imwrite(str(word_list_num)+'/'+str(counter)+'.png', img)

    ser.write(str.encode('scroll'))

    time.sleep(2)

    # string = ser.read(4)
    # print(string)

    print(str(word_list_num)+'/'+str(counter)+'.png')

    counter += 1


