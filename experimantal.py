import gdal
from gdal import Open
from ndwi import ndwi

"""
Using the following function should be as following:

1. Add file path of band for first_band.
2. Add file path of band for second_band.
3. Rely on the results of 32-bit the most.
4. NDVI 1st band Green, 2nd band NIR.
5. NDWI 1st bamd NIR, 2nd Red.
6. Experimantal 1st Green 2nd Red, and vise versia as well, only for the experimnt purpose
"""

def start():
    user_input = input('Enter file path for first_band: ')
    # Open First image and get its only band.
    # first_tiff = Open(r'51/AST_L1B_00308132001191022_20110122163617_24451_ImageData1_b30de2ff.tif')
    first_tiff = Open(user_input)
    first_band = first_tiff.GetRasterBand(1)

    user_input = input('Enter file path for second_band of same image: ')
    # Open Second image and get its only band.
    # second_tiff = Open(r'51/AST_L1B_00308132001191022_20110122163617_24451_ImageData2_b30de2ff.tif')
    second_tiff = Open(user_input)
    second_band = second_tiff.GetRasterBand(1)

    # Release from memory
    user_input = None

    # Get the rows and cols from one of the images (both should always be the same)
    rows, cols, geotransform = first_tiff.RasterYSize, first_tiff.RasterXSize, first_tiff.GetGeoTransform()
    print(geotransform)

    # Set an output for a 16-bit unsigned integer (0-255)
    out_tiff_int16 = r'TEST-RESULTS/NDVI_INT16.tif'

    # Set the output for a 32-bit floating point (-1 to 1)
    out_tiff_float32 = r'TEST-RESULTS/NDVI_FLOAT32.tif'

    # Run the function for unsigned 16-bit integer
    ndwi(first_band, second_band, rows, cols, geotransform, out_tiff_int16, gdal.GDT_UInt16)

    # Run the function for 32-bit floating point
    ndwi(first_band, second_band, rows, cols, geotransform, out_tiff_float32, gdal.GDT_Float32)

    print('done')
