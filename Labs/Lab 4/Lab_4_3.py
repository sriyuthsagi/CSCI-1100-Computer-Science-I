from PIL import Image



im = Image.new('RGB', (1000, 360)) 
dist = 31

im1 = Image.open('1.jpg')
im1x = int((im1.size[0] / im1.size[1])*256)
im1 = im1.resize((im1x, 256))
im.paste(im1,(dist,20))
dist = dist + im1.size[0] + 10

im2 = Image.open('2.jpg')
im2x = int((im2.size[0] / im2.size[1])*256)
im2 = im2.resize((im2x, 256))
im.paste(im2,(dist,60))
dist = dist + im2.size[0] + 10

im3 = Image.open('3.jpg')
im3x = int((im3.size[0] / im3.size[1])*256)
im3 = im3.resize((im3x, 256))
im.paste(im3,(dist,20))
dist = dist + im3.size[0] + 10

im4 = Image.open('4.jpg')
im4x = int((im4.size[0] / im4.size[1])*256)
im4 = im4.resize((im4x, 256))
im.paste(im4,(dist,60))
dist = dist + im4.size[0] + 10

im5 = Image.open('5.jpg')
im5x = int((im5.size[0] / im5.size[1])*256)
im5 = im5.resize((im5x, 256))
im.paste(im5,(dist,20))
dist = dist + im5.size[0] + 10

im6 = Image.open('6.jpg')
im6x = int((im6.size[0] / im6.size[1])*256)
im6 = im6.resize((im6x, 256))
im.paste(im6,(dist,60))
dist = dist + im6.size[0] + 10



im.show()
