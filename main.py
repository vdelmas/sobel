#!/usr/bin/python3.8

from PIL import Image
from math import *
import numpy as np
import os
import sys
import sobel_module

#Loading image and converting to "L" mode (greyscale)
path, name = os.path.split(sys.argv[1])
path = os.getcwd() + os.sep + path
bare_name = name.split(".")[0]
im = Image.open(sys.argv[1]).convert("L")
imar = np.asfortranarray(im, dtype=np.int32)
print(imar.shape)
print(type(imar[0][0]))

(w, h) = im.size

imx_out = Image.new("L",im.size)
imarx_out = np.zeros((h,w),dtype=np.int32,order='F')

imy_out = Image.new("L",im.size)
imary_out = np.copy(imar)
imary_out = np.zeros((h,w),dtype=np.int32,order='F')

imxy_out = Image.new("L",im.size)
imarxy_out = np.zeros((h,w),dtype=np.int32,order='F')

sobel_module.sobel(h, w, imar, imarx_out, imary_out, imarxy_out)

imx_out = Image.fromarray(np.ascontiguousarray(np.uint8(imarx_out)),mode="L")
imy_out = Image.fromarray(np.ascontiguousarray(np.uint8(imary_out)),mode="L")
imxy_out = Image.fromarray(np.ascontiguousarray(np.uint8(imarxy_out)),mode="L")
    
imx_out.save(path+os.sep+bare_name+"_edge_x.jpeg","jpeg")
imy_out.save(path+os.sep+bare_name+"_edge_y.jpeg","jpeg")
imxy_out.save(path+os.sep+bare_name+"_edge_xy.jpeg","jpeg")
