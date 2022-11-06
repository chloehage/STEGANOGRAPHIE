"""
Spyder Editor

This is a temporary script file.
"""

from PIL.Image import *
from PIL import Image

img_fake = open("gouv.jpg")
img_cacher = open("illuminati.jpg")

'''
img_coder = open("image3.png")
img_decoder = open("image4.png") #créer un truc pour que a chaque fois qu'on utilise decoder on recréer une image img_decoderx
img_decoder1 = open("image5.png")
'''

list_pixel = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
lpixels_separation_img = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
lpixels_separation_img2 = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

pixels_image = img_fake.size
pixels_image1 = img_cacher.size


## TODO: remove this unused code
"""
def placer_pixels():
    rconv = int(list_pixel[0])
    vconv = int(list_pixel[1])
    bconv = int(list_pixel[2])
    img.putpixel(x,y),(rconv, vconv, bconv)
"""

def cacher(image_front, image_back):
    pixels_image = image_front.size
    img_coder = Image.new(mode="RGB", size=(pixels_image))
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            (r_fake, v_fake, b_fake) = image_front.getpixel((x,y))
            r_wait = bin(r_fake)
            v_wait = bin(v_fake)
            b_wait = bin(b_fake) # pas dans une liste
            r_fort = r_wait[2:7] #a mettre dans une liste pour pouvoir le manipuler ?
            v_fort = v_wait[2:7]
            b_fort = b_wait[2:7]
            (r2_cacher, v2_cacher, b2_cacher) = image_back.getpixel((x,y))
            r2_wait = bin(r2_cacher)
            v2_wait = bin(v2_cacher)
            b2_wait = bin(b2_cacher)
            r2_fort = r2_wait[2:5]
            v2_fort = v2_wait[2:5]
            b2_fort = b2_wait[2:5]
            r = int(str(r_fort) + str(r2_fort))
            v = int(str(v_fort) + str(v2_fort))
            b = int(str(b_fort) + str(b2_fort))
            list_pixel[0] = r
            list_pixel[1] = v
            list_pixel[2] = b
            rconv = int(list_pixel[0])
            vconv = int(list_pixel[1])
            bconv = int(list_pixel[2])
            img_coder.putpixel((x,y),(rconv, vconv, bconv))
    img_coder.save('img_code.jpg')
    img_coder.show()

    
cacher(img_fake, img_cacher)
img_coder = open('img_code.jpg')

def decoder(img_coder) :
    pixels_image = img_coder.size
    img_decoder = Image.new(mode="RGB", size=(pixels_image))
    img_decoder1 = Image.new(mode="RGB", size=(pixels_image))
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            pixels_wait_coder = img_coder.getpixel((x,y))
            rc_wait = bin(pixels_wait_coder[0])
            vc_wait = bin(pixels_wait_coder[1])
            bc_wait = bin(pixels_wait_coder[2])
            r3_fort = rc_wait[2:7]
            v3_fort = vc_wait[2:7]
            b3_fort = bc_wait[2:7]
            r3_faible = rc_wait[7:]
            v3_faible = vc_wait[7:]
            b3_faible = bc_wait[7:]
            lpixels_separation_img[0][:4] = r3_fort
            lpixels_separation_img[1][:4] = v3_fort
            lpixels_separation_img[2][:4] = b3_fort
            lpixels_separation_img2[0][4:] = r3_faible
            lpixels_separation_img2[1][4:] = v3_faible
            lpixels_separation_img2[2][4:] = b3_faible
            rconv = int(str(lpixels_separation_img[0]),2)
            vconv = int(str(lpixels_separation_img[1]),2)
            bconv = int(str(lpixels_separation_img[2]),2)
            img_decoder.putpixel((x,y),(rconv, vconv, bconv))
            rconv1 = int(str(lpixels_separation_img2[0]),2)
            vconv1 = int(str(lpixels_separation_img2[1]),2)
            bconv1 = int(str(lpixels_separation_img2[2]),2)
            img_decoder1.putpixel((x,y),(rconv1, vconv1, bconv1))
    img_decoder.show()
    img_decoder1.show()


decoder(img_coder)



