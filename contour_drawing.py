
### Filtiring out the coast line

import cv2
import numpy as np
# import imutils

#
# def find_coastline(img_gray, img_rgb):
#     CANNY_THRSH_LOW = 1000
#     CANNY_THRSH_HIGH = 2000
#     # add borders for polygons
#     edge = cv2.Canny(img_gray, CANNY_THRSH_LOW, CANNY_THRSH_HIGH, apertureSize=5)
#     kern = np.ones((5, 5))
#     # dilatation connects most of the disparate edges
#     edge = cv2.dilate(edge, kern)
#     vis = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
#     vis[edge != 0] = (0, 255, 0)
#     cv2.imwrite('boats_canny.jpg', vis)
#     # only external contours
#     contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     vis = np.zeros((img_rgb.shape), np.uint8)
#     i = 0
#     for cnt in contours:
#         color = np.random.random_integers(255, size=(3))
#         cv2.drawContours( vis, contours, i, color,
#                           3, cv2.LINE_AA, hierarchy, 0)
#         i += 1
#     cv2.imwrite('boats_contours.jpg', vis)
#
#

def f_c(img_gray, img_rgb):
    CANNY_THRSH_LOW = 100 #450
    CANNY_THRSH_HIGH = 200 #650
    # img_gray = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    edge = cv2.Canny(img_gray, CANNY_THRSH_LOW, CANNY_THRSH_HIGH, apertureSize=5)
    kern = np.ones((3, 3))
    # dilatation connects most of the disparate edges
    edge = cv2.dilate(edge, kern)
    # invert edges to create one big water blob
    edge_inv = np.zeros((img_gray.shape), np.uint8)
    edge_inv.fill(255)
    edge_inv = edge_inv - edge
    contours0, hierarchy0 = cv2.findContours(edge_inv.copy(), cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)

    vis = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    vis[edge != 0] = (0, 255, 0)
    cv2.imwrite('boats_contours.jpg', vis)


# # c = cv2.imread('~Desktop/2-aster/2-aster-org.jpg')

# # c = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
img_r = cv2.imread('F/12.jpg')
img_g = cv2.imread('S/84.jpg', 0)
# img_g = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
f_c(img_g, img_r)
# find_coastline(img_g, img_r)
# f_c2(img_g)

 Canny  high
gray = cv2.cvtColor(img_g, cv2.COLOR_BGR2GRAY)

# Using the Canny filter to get contours
edges = cv2.Canny(gray, 20, 30)
# Using the Canny filter with different parameters
edges_high_thresh = cv2.Canny(gray, 60, 120)
# Stacking the images to print them together
# For comparison
images = np.hstack((gray, edges, edges_high_thresh))

# Display the resulting frame
cv2.imshow('Frame', images)
cv2.waitKey(0)
