
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
lpixels_separation_img = [['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0']]
lpixels_separation_img2 = [['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0']]
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
            # on récupère les pixels à la position x,y de image_front
            (r_fake, v_fake, b_fake) = image_front.getpixel((x,y)) 
            # conversion du code RVB en binaire
            r_wait = bin(r_fake)
            v_wait = bin(v_fake)
            b_wait = bin(b_fake) 
            # découpage du code RVB pour récupérer les 5 bits de point fort
            r_fort = r_wait[2:7]
            v_fort = v_wait[2:7]
            b_fort = b_wait[2:7]
            # on récupère les pixels à la position x,y de image_back
            (r2_cacher, v2_cacher, b2_cacher) = image_back.getpixel((x,y))
            # conversion du code RVB en binaire
            r2_wait = bin(r2_cacher)
            v2_wait = bin(v2_cacher)
            b2_wait = bin(b2_cacher)
            # découpage du code RVB pour récupérer les 3 bits de point faible
            r2_fort = r2_wait[2:5]
            v2_fort = v2_wait[2:5]
            b2_fort = b2_wait[2:5]
            # on assemble les 5 bits de image_front et les 3 de image_back 
            r = int(str(r_fort) + str(r2_fort))
            v = int(str(v_fort) + str(v2_fort))
            b = int(str(b_fort) + str(b2_fort))
            # assemblage du code RVB pour l'image finale
            list_pixel[0] = r
            list_pixel[1] = v
            list_pixel[2] = b
            # reconversion en décimal
            rconv = int(list_pixel[0])
            vconv = int(list_pixel[1])
            bconv = int(list_pixel[2])
            # formation du pixel sur l'image finale
            img_coder.putpixel((x,y),(rconv, vconv, bconv))
    img_coder.save('img_code.jpg')
    img_coder.show()

    
cacher(img_fake, img_cacher)
img_code = open('img_code.jpg')

def decoder(img_coder) :
    pixels_image = img_coder.size
    img_decoder = Image.new(mode="RGB", size=(pixels_image))
    img_decoder1 = Image.new(mode="RGB", size=(pixels_image))
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            # on récupère le pixel à la position x,y de img_coder
            pixels_wait_coder = img_coder.getpixel((x,y))
            rc_wait = bin(pixels_wait_coder[0])
            vc_wait = bin(pixels_wait_coder[1])
            bc_wait = bin(pixels_wait_coder[2])
            # on récupère les bits de la première image
            r3_fort = rc_wait[2:7]
            v3_fort = vc_wait[2:7]
            b3_fort = bc_wait[2:7]
            # on récupère les bits de la deuxième image
            r3_faible = rc_wait[7:]
            v3_faible = vc_wait[7:]
            b3_faible = bc_wait[7:]
            # formation du code RVB de chaque image
            lpixels_separation_img[0][:4] = r3_fort
            lpixels_separation_img[1][:4] = v3_fort
            lpixels_separation_img[2][:4] = b3_fort
            lpixels_separation_img2[0][:4] = r3_faible
            lpixels_separation_img2[1][:4] = v3_faible
            lpixels_separation_img2[2][:4] = b3_faible
            # conversion de la liste en chaine de caractère 
            rchaine = ''.join(lpixels_separation_img[0])
            vchaine = ''.join(lpixels_separation_img[1])
            bchaine = ''.join(lpixels_separation_img[2])
            # conversion en décimal
            rconv = int(rchaine,2)
            vconv = int(vchaine,2)
            bconv = int(bchaine,2)
            img_decoder.putpixel((x,y),(rconv, vconv, bconv))
            rchaine1 = ''.join(lpixels_separation_img2[0])
            vchaine1 = ''.join(lpixels_separation_img2[1])
            bchaine1 = ''.join(lpixels_separation_img2[2])
            rconv1 = int(rchaine1,2)
            vconv1 = int(vchaine1,2)
            bconv1 = int(bchaine1,2)
            img_decoder1.putpixel((x,y),(rconv1, vconv1, bconv1))
    img_decoder.show()
    img_decoder1.show()


decoder(img_code)



