from PIL import Image, ImageDraw
from image import Img
from math import sqrt


img = Img("./obama.jpg")

width, height = img.img.size

resize_factor = width // 90
if resize_factor < 1:
    resize_factor = 1
img.get_pixel_array(resize_factor)
data = img.pixels
width = len(img.pixels)
height = len(img.pixels[0])

def scale(val, in_min, in_max, out_range=[0, 12]):
    scale_around_zero = (val - (in_min + in_max) / 2) / (in_max - in_min)
    return scale_around_zero * (out_range[1] - out_range[0]) + (out_range[1] + out_range[0]) / 2

def get_luminance(pixel):
    return sqrt(0.299*pixel[0]**2 + 0.587*pixel[1]**2 + 0.114*pixel[2]**2 )

def to_ascii(lum, min_val, max_val):
    scaled_val = scale(lum, min_val, max_val)
    vals = [".", ",", "-", "~", ":", ";", "=", "!", "*", "#", "$", "@"]
    val = round(scaled_val)
    if val > 0:
        return vals[val-1]
    else:
        return vals[0]

new_img = []
for y in range(height):
    row = []
    for x in range(width):
        val = data[x][y]
        row.append(get_luminance(val))
    new_img.append(row)

min_val = new_img[0][0]
max_val = new_img[0][0]
for row in new_img:
    minv = min(row)
    maxv = max(row)
    if maxv > max_val:
        max_val = maxv
    if minv < min_val:
        min_val = minv

#new_img = new_img[::-1]
for row in new_img:
    for pixel in row:
        print (to_ascii(pixel, min_val, max_val), end="")
    print ()
