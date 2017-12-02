from PIL import Image, ImageOps
import cv2
import os.path

ORI_PATH = "3D_images"

def file_name(t, z):
  return "t={:02d}_z={:03d}.jpg".format(t, z)

def img_process(path):
  img = Image.open(path)
  img = ImageOps.invert(img)
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 255 and item[2] == 255:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  img.putdata(newData)
  return img

def main():
  for t in range(1, 21):
    output_path = "overlay"
    if not os.path.exists(output_path):
      os.mkdir(output_path)
    for z in range(1, 101):
      path = file_name(t, z)
      if z == 1:
        img = img_process(path)
      else:
        im2 = img_process(path)
        img.paste(im2)
        img.save("{}/{}.png".format(output_path, t), "PNG")


def denoise(filepath, output_path):
    image = cv2.imread(filepath)
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
  for t in range(1, 21):
    output_path = "denoise"
    if not os.path.exists(output_path):
      os.mkdir(output_path)
    for z in range(1, 101):
      filepath = "{}/{}".format(ORI_PATH, file_name(t, z))
      output_path = "{}/{}".format(output_path, file_name(t, z))
      denoise(filepath, output_path)
