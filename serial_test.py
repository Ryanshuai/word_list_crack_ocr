from PIL import ImageGrab
import numpy as np
import time
import cv2
import serial
import time

word_list_num = 7

counter = 0
zero_counter = 0
have_not_save = True
ser = serial.Serial('com5', 9600)

while True:

    # img = np.array(ImageGrab.grab(bbox=(1, 329, 610, 1390)))
    img = np.array(ImageGrab.grab())
    cv2.imwrite(str(word_list_num)+'/'+str(counter)+'.png', img)

    ser.write(str.encode('scroll'))

    string = ser.read(4)
    print(string)



