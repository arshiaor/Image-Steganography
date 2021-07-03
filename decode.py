from PIL import Image


def decode():
    image = input("Enter image name (with extention): ")
    image = Image.open(image, 'r')

    data = ''
    imageData = iter(image.getdata())

    while (True):
        pixels = [value for value in imageData.__next__()[:3] + imageData.__next__()[:3] + imageData.__next__()[:3]]

        # string of binary data that will be converted to characters
        binaryString = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binaryString += '0'
            else:
                binaryString += '1'
        data += chr(int(binaryString, 2))
        if pixels[-1] % 2 != 0:
            return data
