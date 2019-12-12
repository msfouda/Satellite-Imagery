
 # This Code is yo open and review source images and references

import scipy
import sklearn
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def asterData(imgNumber,axs):
    AsterImages = loadmat('SatData.mat',variable_names='AsterData',appendmat=True).get('AsterData')
    # print(AsterImages)
    imgplot = axs[0].imshow(AsterImages[:,:,imgNumber - 1])
    axs[0].set_xlabel('AsterImage')

def asterRef(imgNumber, axs):
    RefImages = loadmat('referenceMaps.mat',variable_names='AsterRefMap',appendmat=True).get('AsterRefMap')
    # print(RefImages)
    imgplot = axs[1].imshow(RefImages[0][imgNumber - 1])
    axs[1].set_xlabel('RefImages')

def show_fig():
    x = int(input("Enter image number: "))
    fig, axs = plt.subplots(1, 2)
    asterRef(x, axs)
    asterData(x, axs)

    fig.patch.set_visible(False)
    axs[0].axis('off')
    axs[1].axis('off')
    plt.ion()
    # Uncomment following line to save results into .png
    # plt.savefig(r'TEST-RESULTS/REVIEW-image-' + str(x) + '.png')
    plt.show()
    check();

def check():
    s = input('Enter x to close, or n to show other images:  ')
    if s == 'x':
        plt.close()
    elif s == 'n':
        plt.close()
        show_fig()
