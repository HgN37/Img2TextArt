from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage.transform import resize
from matplotlib import pyplot as plt
from skimage.exposure import is_low_contrast

from text2img import text2img
from img2text import img2text

import sys, getopt

def main(sys_arg):
    try:
        opts, args = getopt.getopt(sys_arg,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    input_file = ''
    output_file = ''

    for opt, arg in opts:
        if opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
    
    #TODO: Implement more inline parameter
    #TODO: Asset parameter

    txt_out_file = img2text(input_file)
    img_out_file = text2img(txt_out_file, output_file)
    print('Successfully create new ASCII art: ', img_out_file)
    return img_out_file

if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(0)