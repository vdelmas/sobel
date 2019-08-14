#!/usr/bin/python3.6

from PIL import Image

im = Image.open("ets.jpeg").convert("L")
(w, h) = im.size
im_out = Image.new("L",im.size)

for i in range(1,w-1):
  for j in range(1,h-1):
    valuex = 2*im.getpixel((i-1,j))
    valuex += im.getpixel((i-1,j))
    valuex += im.getpixel((i+1,j))
    valuex -= 2*im.getpixel((i,j-1))
    valuex -= im.getpixel((i,j+1))
    valuex -= im.getpixel((i,j-1))
    im_out.putpixel((i,j),valuex)
    
#im_out.show()
im_out.save("ets_edges.jpeg","jpeg")
