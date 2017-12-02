from PIL import Image, ImageOps
import cv2
import os.path
from tqdm import tqdm

ORI_PATH = "3D_images"


def file_name(t, z):
    return "t={:02d}_z={:03d}.jpg".format(t, z)


def denoise(input_path , output_path):
    image = cv2.imread(input_path)
    # dst = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # threshold the image to reveal light regions in the
    # blurred image
    thresh = cv2.threshold(blurred, 25, 255, cv2.THRESH_BINARY)[1]
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    cv2.imwrite(output_path, thresh)


if __name__ == '__main__':
    output_dir = "denoise"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for t in tqdm(range(1, 21)):
        for z in range(1, 101):
            input_path = "{}/{}".format(ORI_PATH, file_name(t, z))
            print(input_path)
            output_path = "{}/{}".format(output_dir, file_name(t, z))
            denoise(input_path , output_path)
