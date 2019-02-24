import cv2
import numpy as np
import os


def correct_line_num(im0, im1):
    mina = 1e10
    mini = 0
    for i in range(350, 375):

        tile0 = im0[-i:, :, :]
        tile1 = im1[:i, :, :]

        # cv2.imshow('0',tile0)
        # cv2.waitKey(0)
        # cv2.imshow('1',tile1)
        # cv2.waitKey(0)

        sum_sub = np.sum(tile0-tile1)
        average_sum_sub = sum_sub/i

        if average_sum_sub < mina:
            mina = average_sum_sub
            mini = i

    print(mini)
    return mini
    #     print(i, average_sum_sub)
    # print(mina)


def merge_image(im0, im1):
    line_num = correct_line_num(im0, im1)
    # if line_num < 355 or line_num > 365:
    #     cv2.imshow('im0', im0)
    #     cv2.waitKey()
    #     cv2.imshow('im1', im1)
    #     cv2.waitKey()

    new_im = np.concatenate((im0, im1[line_num:]))

    # cv2.imshow('new', new_im)
    # cv2.waitKey(0)
    return new_im


def merge_fold_num(word_list_num):
    dir_len = len(os.listdir(str(word_list_num)))

    res_im = cv2.imread(str(word_list_num) + '/' + str(0) + '.png')
    for i in range(1, dir_len):
        # print(i)
        im_name = str(word_list_num) + '/' + str(i) + '.png'
        append_im = cv2.imread(im_name)

        if append_im is None:
            continue

        res_im = merge_image(res_im, append_im)

    cv2.imwrite(str(word_list_num) + '.png', res_im)
    return res_im


if __name__ == '__main__':
    word_list_num = 3
    dir_len = len(os.listdir(str(word_list_num)))

    res_im = cv2.imread(str(word_list_num)+'/'+str(0)+'.png')
    for i in range(1, dir_len):
        # print(i)
        im_name = str(word_list_num)+'/'+str(i)+'.png'
        append_im = cv2.imread(im_name)

        if append_im is None:
            continue

        res_im = merge_image(res_im, append_im)

    cv2.imwrite(str(word_list_num)+'.png', res_im)
