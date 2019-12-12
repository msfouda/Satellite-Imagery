import review_source
import threshold_cv_only
import itrative_threshold_GDAL
import experimantal

user_input = int(input('Choose which mode you like to run from\n 1) review_source\n 2) threshold_cv_only\n 3) itrative_threshold_GDAL\n 4) NDWI\n 1,2,3 or 4: '))

if user_input == 1:
    review_source.show_fig()
elif user_input == 2:
    threshold_cv_only.start()
elif user_input == 3:
    itrative_threshold_GDAL.start()
elif user_input == 4:
    experimantal.start()
