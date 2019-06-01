from PIL import Image

def make_square(img):
    im = Image.open(img)
    immin = min(im.size)
    im = im.crop((0, 0, immin, immin))
    return im

