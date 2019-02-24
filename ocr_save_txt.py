from PIL import Image
import pytesseract
import numpy as np
import cv2
from autocorrect import spell
import re


word_list_im_name = 5

def filter_word(word):
    cop = re.compile("[^\[\]^a-z^A-Z^0-9^\-^:]") # 匹配不是中文、大小写、数字的其他字符
    word = cop.sub(' ', word) #将string1中匹配到的字符替换成空字符
    return word

def not_in_alphabet(word):
    word_list = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in word:
        if i not in word_list:
            return True
    return False


img = cv2.imread(str(word_list_im_name)+'.png', 0)
base_line = np.mean(img[:, 5:20], axis=1)


ground_y = 0
# ground_y = 3560

word_list = []

while True:
    # if ground_y >= 1000:
    #     break
    if ground_y >= len(base_line):
        break
    color = base_line[ground_y]

    if 70 < color:
        main_color = base_line[ground_y + 50]
        if main_color < 70:
            word_im = img[ground_y+15:ground_y+50, 20:600]
            # words = pytesseract.image_to_string(word_im, config='word_list')
            ret, word_im = cv2.threshold(word_im, 127, 255, cv2.THRESH_BINARY)
            word_im = 255 - word_im
            word = pytesseract.image_to_string(word_im, config="-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")
            # words = pytesseract.image_to_string(word_im, boxes=False, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            print(ground_y, word)

            if spell(word) != word or not_in_alphabet(word):
                cv2.imshow('word', word_im)
                cv2.waitKey(0)
                word = input("input the correct word:")

            word_list.append(word)
            ground_y += 80

            # cv2.imshow('word', word_im)
            # cv2.waitKey(0)

        if 100 < main_color:
            word_im = img[ground_y+15:ground_y+65, 20:600]
            ret, lead_im = cv2.threshold(word_im, 127, 255, cv2.THRESH_BINARY)
            word_im = 255 - word_im
            word = pytesseract.image_to_string(word_im, config="-c tessedit_char_whitelist=0123456789[]-.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")
            word = filter_word(word)
            print(word)
            word_list.append(word)

            ground_y += 72

            # cv2.imshow('word', word_im)
            # cv2.waitKey(0)

            word_im = img[ground_y+15:ground_y+50, 20:600]
            # words = pytesseract.image_to_string(word_im, config='word_list')

            ret, word_im = cv2.threshold(word_im, 127, 255, cv2.THRESH_BINARY)
            word_im = 255 - word_im
            word = pytesseract.image_to_string(word_im, config="-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")
            # words = pytesseract.image_to_string(word_im, boxes=False, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            print(ground_y, word)

            word_list.append(word)
            ground_y += 80

            if spell(word) != word or not_in_alphabet(word):
                cv2.imshow('word', word_im)
                cv2.waitKey(0)
                word = input("input the correct word:")

            # cv2.imshow('word', word_im)
            # cv2.waitKey(0)

    ground_y += 1

with open("word_list"+str(word_list_im_name)+".txt", "w") as f:
    for word in word_list:
        f.write(word)
        f.write('\n')