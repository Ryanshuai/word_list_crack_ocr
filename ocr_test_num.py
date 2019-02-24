from PIL import Image
import pytesseract
import numpy as np
import cv2
from autocorrect import spell
from merge_image import merge_fold_num


word_list_num = 5
merge_fold_num(word_list_num)

img = cv2.imread(str(word_list_num)+'.png', 0)
base_line = np.mean(img[:, 5:20], axis=1)

ground_y = 0
# ground_y = 29000
counter = 2

while True:
    # if ground_y >= 1000:
    #     break
    if ground_y >= len(base_line):
        break
    color = base_line[ground_y]

    if 100 < color:
        word_im = img[ground_y+15:ground_y+65, 20:600]
        # ret, lead_im = cv2.threshold(lead_im, 127, 255, cv2.THRESH_BINARY)
        word = pytesseract.image_to_string(word_im, config="-c tessedit_char_whitelist=0123456789[]-.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")
        ground_y += 73

        print(ground_y, word)

        if str(counter) in word:
            print(counter)

        counter += 1

    ground_y += 1

