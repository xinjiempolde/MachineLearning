import cv2
import os
import math


def del_noise(im_cut):
    th1 = cv2.adaptiveThreshold(im_cut, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    return th1


def cut_img(im_path, pos, name_list):
    # 读取图片
    # 相对路径要写..不然会报错NoneType
    im = cv2.imread(im_path)

    # 灰度化
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # 剪切
    cut_img_1 = gray[6:25, 3:15]
    cut_img_2 = gray[6:25, 20:32]
    cut_img_3 = gray[6:25, 36:48]
    cut_img_4 = gray[6:25, 53:65]

    cut_img_list = [cut_img_1, cut_img_2, cut_img_3, cut_img_4]
    for i in range(len(cut_img_list)):
        img_tmp = del_noise(cut_img_list[i])
        cv2.imwrite('./img_train_cut/' + str(pos) + '_' + str(i) + '_' + name_list[i] + '.jpg', img_tmp)


if __name__ == '__main__':
    img_dir = './RawImg'
    img_name = os.listdir(img_dir)
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        name_list = list(img_name[i])[:4]
        print('处理%s' % img_name[i])
        cut_img(path, i, name_list)
