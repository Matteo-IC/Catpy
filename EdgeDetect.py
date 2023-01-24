import cv2 as cv


def image_edges():

    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = 'e'

    image = 'cat.jpg'
    src = cv.imread(cv.samples.findFile(image), cv.IMREAD_COLOR)

    src = cv.GaussianBlur(src, (3, 3), 0)
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    apply_laplace = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)

    converted = cv.convertScaleAbs(apply_laplace)

    cv.imwrite('cat_with_edges.png', converted)

    return converted


if __name__ == "__main__":
    image_edges()
