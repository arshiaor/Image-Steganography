from PIL import Image


# use 8-bit binary encoding
# use ASCII value of characters
def generateData(data):
    newData = []
    # contains binary code of given message

    for i in data:
        newData.append(format(ord(i), '08b'))
    return newData


# modify and return all pixels according to 8-bit binary data
def modifyPixels(pix, data):
    datalist = generateData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        # extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]


        #pixel valuses should be compared as odd for 1 and even to 0
        for j in range(0, 8):
            if datalist[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1
            elif datalist[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1


        # this is eighths pixel of every set that says whether to stop reading or not
        # if its 0 means keep reading else ( if its 1) means stop
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modifyPixels(newimg.getdata(), data):

        newimg.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


def encode():
    image = input("enter image name(with extention): ")
    image = Image.open(image, 'r')

    data = input("put the message you want : ")
    if len(data) == 0:
        raise ValueError('Empty Data')

    newImage = image.copy()
    encode_enc(newImage, data)

    new_image_name = input("enter new name for image(with extention): ")
    newImage.save(new_image_name, str(new_image_name.split(".")[1].upper()))
