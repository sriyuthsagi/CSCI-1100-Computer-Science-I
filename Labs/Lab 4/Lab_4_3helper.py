from PIL import Image

def imgedit(img, im, dist):
    im1 = Image.open(img)
    im1x = int((im1.size[0] / im1.size[1])*256)
    im1 = im1.resize((im1x, 256))
    im.paste(im1,(dist,20))
    dist = dist + im1.size[0] + 10  
    return img, im, dist