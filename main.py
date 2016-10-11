from PIL import Image
import math
import Graph_lib as g

white=(255,255,255,255)

"""image=Image.new("RGBA",(500,500),(0,0,0,255))
image1=Image.new("RGBA",(500,500),(0,0,0,255))
g.Bresenham(100,50,400,200,white,image)
g.Bresenham(100,50,400,25,white,image)
g.Bresenham(400,25,400,200,white,image)

g.Bresenham(100,50,400,200,white,image1)
g.Bresenham(100,50,400,25,white,image1)
g.Bresenham(400,25,400,200,white,image1)
image.save("Fill.bmp")

points=dict()
a=g.foreach(100,50,400,200,points)
b=g.foreach(100,50,400,25,a)
c=g.foreach(400,25,400,200,b)


g.fill_str(c,image,white,"str_fill.bmp")
image1.putpixel((150,50),white)
g.fill_seed((150,50),white,white,image1,"Fill.bmp");
g.obj_plotter("african_head.obj")
"""
print(g.cohen_sutherland(250,250,400,400,500,500,0,0))
print(g.cohen_sutherland(500,600,500,800,500,500,0,0))
print(g.cohen_sutherland(-5,250,600,250,500,500,0,0))
print(g.cohen_sutherland(-5,-50,600,600,500,500,0,0))
print("------------------------------------------")
print(g.liang_barski(250,250,400,400,0,500,0,500))
print(g.liang_barski(500,600,500,800,0,500,0,500))
print(g.liang_barski(-5,250,600,250,0,500,0,500))
print(g.liang_barski(-5,-50,600,600,0,500,0,500))
