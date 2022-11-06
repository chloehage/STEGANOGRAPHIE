# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from email.mime import image
from PIL.Image import *

img_fake = open("image0.png")
img_cacher = open("image2.png")
img_coder = open("image3.png")
img_decoder = open("image4.png") #créer un truc pour que a chaque fois qu'on utilise decoder on recréer une image img_decoderx
img_decoder1 = open("image5.png")

list_pixel = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
lpixels_separation_img = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
lpixels_separation_img2 = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

pixels_image = img_fake.size
pixels_image1 = img_cacher.size
pixels_image2 = img_coder.size

## TODO: remove this unused code
"""
def placer_pixels():
    rconv = int(list_pixel[0])
    vconv = int(list_pixel[1])
    bconv = int(list_pixel[2])
    img.putpixel(x,y),(rconv, vconv, bconv)
"""

def cacher(image_front, image_back):
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            (r_fake, v_fake, b_fake) = image_front.getpixel((x,y))
            r_wait = bin(r_fake)
            v_wait = bin(v_fake)
            b_wait = bin(b_fake) # pas dans une liste
            r_fort = r_wait[:4] #a mettre dans une liste pour pouvoir le manipuler ?
            v_fort = v_wait[:4]
            b_fort = b_wait[:4]
            (r2_cacher, v2_cacher, b2_cacher) = image_back.getpixel((x,y))
            r2_wait = bin(r2_cacher)
            v2_wait = bin(v2_cacher)
            b2_wait = bin(b2_cacher)
            r2_fort = r2_wait[:4]
            v2_fort = v2_wait[:4]
            b2_fort = b2_wait[:4]
            list_pixel[0][:4] = r2_fort # un .append est necessaire je pense
            list_pixel[0][5:] = r_fort
            list_pixel[1][:4] = v2_fort
            list_pixel[1][5:] = v_fort
            list_pixel[2][:4] = b2_fort
            list_pixel[2][5:] = b_fort
            rconv = int(list_pixel[0])
            vconv = int(list_pixel[1])
            bconv = int(list_pixel[2])
            img_coder.putpixel(x,y),(rconv, vconv, bconv)

def decoder() :
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            pixels_wait_coder = img_coder.getpixels((x,y))
            rc_wait = bin(pixels_wait_coder[0])
            vc_wait = bin(pixels_wait_coder[1])
            bc_wait = bin(pixels_wait_coder[2])
            r3_fort = rc_wait[:4]
            v3_fort = vc_wait[:4]
            b3_fort = bc_wait[:4]
            lpixels_separation_img[0][:4] = r3_fort
            lpixels_separation_img[1][:4] = v3_fort
            lpixels_separation_img[2][:4] = b3_fort
            r3_faible = rc_wait[5:]
            v3_faible = vc_wait[5:]
            b3_faible = bc_wait[5:]
            lpixels_separation_img2[0][:4] = r3_faible
            lpixels_separation_img2[1][:4] = v3_faible
            lpixels_separation_img2[2][:4] = b3_faible
            rconv = int(lpixels_separation_img[0])
            vconv = int(lpixels_separation_img[1])
            bconv = int(lpixels_separation_img[2])
            img_decoder.putpixel(x,y),(rconv, vconv, bconv)
            rconv1 = int(lpixels_separation_img2[0])
            vconv1 = int(lpixels_separation_img2[1])
            bconv1 = int(lpixels_separation_img2[2])
            img_decoder1.putpixel(x,y),(rconv1, vconv1, bconv1)

## TODO: Use the coder() function to encode the image
decoder()

img.show() # TODO: Change the variable name