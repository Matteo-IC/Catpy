import cv2 as cv
from PIL import Image

max_lowThreshold = 100
window_name = 'Edge Map'
title_trackbar = 'Min Threshold:'
ratio = 3
kernel_size = 3
src = cv.imread(cv.samples.findFile(args.input))
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)


def CannyThreshold(val):
    low_threshold = val
    img_blur = cv.blur(src_gray, (3,3))
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    mask = detected_edges != 0
    dst = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, dst)

    return dst

CannyThreshold(0)
cv.waitKey()

if __name__ == "__main__":
    CannyThreshold()
