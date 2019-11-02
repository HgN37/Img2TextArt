from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage.transform import resize
from matplotlib import pyplot as plt
from skimage.exposure import is_low_contrast

default_map = ('@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', ' ')

def img2text(img_in, txt_out='temp.txt', resize_img=(128,256), map=default_map):
    img = imread(img_in)
    img = rgb2gray(img)

    if (resize is not False):
        imgage_resized = resize(img, resize_img, anti_aliasing=True)
    
    with open(txt_out, 'w') as txt:
        for row in imgage_resized:
            line = ''
            for dot in row:
                value = int(dot*(len(map)-1))
                line += map[value]
            txt.write(line + '\r\n')
    return txt_out

if __name__ == '__main__':
    # TO TEST
    img = imread('./avatar.jpg')
    img = rgb2gray(img)

    image_resized = resize(img, (128, 256),
                        anti_aliasing=True)

    print(is_low_contrast(image_resized))

    with open('./text.txt', 'w') as txt:
        for row in image_resized:
            line = ''
            for dot in row:
                value = int(dot*11)
                line += default_map[value]
            txt.write(line + '\r\n')


