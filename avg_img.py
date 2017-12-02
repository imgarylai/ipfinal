import os, numpy, PIL
from PIL import Image

DE_PATH = "denoise"
AVG_PATH = "avg"

def average_img(imlist):
    # Alternative method using numpy mean function
    images = numpy.array([numpy.array(Image.open(fname)) for fname in imlist])
    arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    return out

if __name__ == '__main__':

    for i in range(1, 21):
        subdir_path = "{}/{}".format(DE_PATH, i)
        allfiles = os.listdir(subdir_path)
        imlist = ["{}/{}".format(subdir_path, filename) for filename in allfiles if filename[-4:] in [".jpg", ".JPG"]]

        out = average_img(imlist)

        out.save("{}/t{}.jpg".format(AVG_PATH, i))
