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