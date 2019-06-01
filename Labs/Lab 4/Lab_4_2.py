import Lab_4_2helper
from PIL import Image

im = Image.new('RGB', (1000,1000)) 
im1 = Lab_4_2helper.make_square('ca.jpg')
im2 = Lab_4_2helper.make_square('im.jpg')
im3 = Lab_4_2helper.make_square('hk.jpg')
im4 = Lab_4_2helper.make_square('bw.jpg')



im.paste(im1,(0,0))
im.paste(im2,(500,0))
im.paste(im3,(0,500))
im.paste(im4,(500,500))
im.show()

