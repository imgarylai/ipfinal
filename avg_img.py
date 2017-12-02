import os, numpy, PIL
from PIL import Image

# Access all PNG files in directory
# allfiles=os.listdir(os.getcwd())
# imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]
#
# # Assuming all images are the same size, get dimensions of first image
# w,h=Image.open(imlist[0]).size
# N=len(imlist)
#
# # Create a numpy array of floats to store the average (assume RGB images)
# arr=numpy.zeros((h,w,3),numpy.float)
#
# # Build up average pixel intensities, casting each image as an array of floats
# for im in imlist:
#     imarr=numpy.array(Image.open(im),dtype=numpy.float)
#     arr=arr+imarr/N
#
# # Round values in array and cast as 8-bit integer
# arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
#
# # Generate, save and preview final image
# out=Image.fromarray(arr,mode="RGB")
# out.save("Average.png")
# out.show()

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
        # N = len(imlist)
        # avg = Image.open(imlist[0])
        # for k in range(1, N):
        #     img = Image.open(imlist[k])
        #     avg = Image.blend(avg, img, 1.0 / float(k+ 1))
        # w, h = Image.open(imlist[0]).size
        # N = len(imlist)
        # arr = numpy.zeros((h, w, 3), numpy.float)
        # for im in imlist:
        #     imarr = numpy.array(Image.open(im), dtype=numpy.float)
        #     arr = arr + imarr / N
        #
        # arr = numpy.array(numpy.round(arr), dtype=numpy.uint8)
        # out = Image.fromarray(arr, mode="RGB")

        out = average_img(imlist)

        out.save("{}/t{}.jpg".format(AVG_PATH, i))
