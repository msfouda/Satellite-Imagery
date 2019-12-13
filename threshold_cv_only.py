
# This file where the thresholding modes live

import scipy
import sklearn
import numpy as np
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# Set root dir to save results
root = r'TEST-RESULTS/'

try:
    images = loadmat('SatData.mat',variable_names='AsterData',appendmat=True).get('AsterData')
except Exception as e:
    print('SatData.mat is not found, specify your SatData source path')
    images = input('Enter SatData Path:')

plt.figure(frameon=False)

# Following method get the image and store it in png
def get_image(imgNumber):
    img = plt.imshow(images[:,:,imgNumber - 1])
    plt.axis('off')
    img_path = 'TIR-' + str(imgNumber) + '.png'
    plt.savefig(root + img_path)
    # plt.show()
    return img_path

def img():
    x = int(input("Enter TIR image number: "))
    img_path = get_image(x)
    return img_path

# print (img())

# #################### #
# Threshold
# #################### #

# following function set dynamic img getter and defult threshold values
def canny_on_gaussian_and_binary(img_path = 'defult', thresh = 11, filter = 'on', with_canny = 'yes', canny_low = 100, canny_high = 200):
    if img_path == 'defult':
        img_path = img()

    # Read image in gray scale
    c = cv2.imread(root + img_path, 0)

    # Apply medianBlur_filter
    if filter == 'on':
        c = cv2.medianBlur(c,5)

    # ADAPTIVE_THRESH_GAUSSIAN with Simple THRESH_BINARY
    c = cv2.adaptiveThreshold(c, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, thresh, 2)

    # Apply Canny edge detection
    if with_canny == 'yes':
        c = cv2.Canny(c, canny_low, canny_high)
    save_path = root + 'CANNY_GAUSSIAN_BINARY-' + img_path
    cv2.imwrite(save_path, c)
    cv2.imshow('img', c)
    cv2.waitKey(3000)

def start():
    user_input = input('Enter canny_on_gaussian_and_binary params or enter to use defults:\n (ex: ImageFilePath,11,on,yes,100,200\n Do not use white spaces\n Ref of attrs: ImageFilePath,THRESH_VALUE,medianBlur_filter,CANNY_ON,CANNY_THRSH_LOW,CANNY_THRSH_HIGH ')
    print('\nClick on the opned image and press any key to close and carry on')
    if user_input is '':
        canny_on_gaussian_and_binary()
    else:
        a = user_input.split(',')
        canny_on_gaussian_and_binary(a[0], int(a[1]), a[2], a[3], int(a[4]), int(a[5]))
    # Keep running code recursoively untill no more checks needed
    check_more = input('Check other image, yes or no: ')
    if check_more == 'yes':
        start()
