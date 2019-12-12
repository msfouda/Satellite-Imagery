import osgeo
import gdal
import cv2
# import rasterio
import numpy as np
# from rasterio.plot import show

# Set root dir to save results
root = r'TEST-RESULTS/'
save_path = root + 'THRESH_GDAL.jpeg'

def thresh_gdal(img_path = 'defult', start_thresh_value = 65, step = 50, auto = 'off'):
    # Fix image_file_path for quick run
    if img_path == 'defult':
        img_path = root + 'TIR-2.png'

    inpuDataset = gdal.Open(img_path)
    format = 'JPEG'
    driver = gdal.GetDriverByName(format)

    # Creat copy of the image to be worked on apart of original input
    outputDataset = driver.CreateCopy(save_path, inpuDataset, 0)

    # Release values
    inpuDataset = None
    outputDataset = None

    # Load image using GDAL ref and OpenCV library in grayscale
    img = cv2.imread(save_path, cv2.IMREAD_LOAD_GDAL & cv2.IMREAD_GRAYSCALE)

    thresh_value = start_thresh_value
    while thresh_value < 255:
        th, processed_image =  cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)

        cv2.imwrite(save_path, processed_image)
        cv2.imshow('thresholded_NDVI', processed_image)
        print('THRESH_VALUE: ' + str(thresh_value))
        if auto == 'off':
            # Wait infinitly for any key press (make sure you on the image window)
            cv2.waitKey(0)
        else:
            cv2.waitKey(500)
        cv2.destroyAllWindows()
        thresh_value = thresh_value + step

def start():
    image_file_path = input('Enter image_file_path or Press Enter for defult: ')
    if image_file_path is '':
        thresh_gdal()
    else:
        value = int(input('Enter start_thresh_value: '))
        step = int(input('Enter step: '))
        auto = input('choose on or off for auto itration mode: ')
        thresh_gdal(image_file_path, value, step, auto)

    # Load Ref Dictionary
    try:
        dict = np.load('GDAL_thresh_dictionary.npy',allow_pickle='TRUE').item()
    except FileNotFoundError:
        # doesn't exist
        print('No previous references found, new one will be created!')
        dict = {}
    else:
        # exists
        print('Check dict below for previous threshold refernces')
        print(dict)

    save_to_dictionary = input('Which Threshold Value to be saved for this image?\n give image number and THRESH_VALUE\n (ex: 2,75) \n Enter: ')
    a = save_to_dictionary.split(',')
    dict[int(a[0])] = int(a[1])
    # print(dict)
    np.save('GDAL_thresh_dictionary.npy', dict)
