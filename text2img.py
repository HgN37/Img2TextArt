from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def text2img(text_in, img_out, size=(1920, 1920), background=(255, 255, 255), text_color=(0, 0, 0), font="UbuntuMono-RI.ttf", font_size=14):
    img = Image.new('RGB', size, background)
    draw = ImageDraw.Draw(img)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, font_size)

    contents = ''
    with open(text_in, 'r') as txt:
        contents = txt.read()
    draw.text((0, 0), contents, text_color, font=font)
    #TODO: Add remove trailing blank space
    img.save(img_out)
    return img_out

if __name__ == '__main__':
    # To test functionality
    mode = 'RGB'
    size = (1920, 1920)
    color = (255, 255, 255)
    font = "UbuntuMono-RI.ttf"
    font_size = 16
    text_in_file = 'text.txt'
    img_out_file = 'out.jpg'

    img = Image.new(mode, size, color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, font_size)

    contents = ''
    with open(text_in_file, 'r') as txt:
        contents = txt.read()

    draw.text((0, 0),contents,(0, 0, 0),font=font)
    img.save(img_out_file)

