#!/usr/bin/python3.6

from PIL import Image
from math import *
import os
import sys

#Loading image and converting to "L" mode (greyscale)
path, name = os.path.split(sys.argv[1])
bare_name = name.split(".")[0]
im = Image.open(sys.argv[1]).convert("L")

(w, h) = im.size
print(w,h)

im_out = Image.new("L",im.size)
imx_out = Image.new("L",im.size)
imy_out = Image.new("L",im.size)
imxy_out = Image.new("L",im.size)

for i in range(1,w-1):
  for j in range(1,h-1):
    #Formule ?
    value = 2*im.getpixel((i-1,j))
    value += im.getpixel((i-1,j))
    value += im.getpixel((i+1,j))
    value -= 2*im.getpixel((i,j-1))
    value -= im.getpixel((i,j+1))
    value -= im.getpixel((i,j-1))
    im_out.putpixel((i,j),value)

    #Formule gradient sobel x
    valuex = 2*im.getpixel((i,j-1))
    valuex += im.getpixel((i-1,j-1))
    valuex += im.getpixel((i+1,j-1))
    valuex -= 2*im.getpixel((i,j+1))
    valuex -= im.getpixel((i-1,j+1))
    valuex -= im.getpixel((i+1,j+1))
    imx_out.putpixel((i,j),valuex)

    #Formule gradient sobel y
    valuey = 2*im.getpixel((i-1,j))
    valuey += im.getpixel((i-1,j+1))
    valuey += im.getpixel((i-1,j-1))
    valuey -= 2*im.getpixel((i+1,j))
    valuey -= im.getpixel((i+1,j+1))
    valuey -= im.getpixel((i+1,j-1))
    imy_out.putpixel((i,j),valuey)

    imxy_out.putpixel((i,j),int(sqrt(valuex**2+valuey**2)/sqrt(2)))
    
#im_out.show()
im_out.save(path+os.sep+bare_name+"_edge.jpeg","jpeg")
imx_out.save(path+os.sep+bare_name+"_edge_x.jpeg","jpeg")
imy_out.save(path+os.sep+bare_name+"_edge_y.jpeg","jpeg")
imxy_out.save(path+os.sep+bare_name+"_edge_xy.jpeg","jpeg")
