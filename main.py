from PIL import Image
import math

white=(255,255,255,255)

def drawpoint(x,y,steep,i,image):
    if steep:
        x,y=y,x
    image.putpixel((x,y),(int(255*i),int(255*i),int(255*i),255))

    print((int(255*i),int(255*i),int(255*i),int(255*i)))
    None


def Bresenham(x1,y1,x2,y2,image):
    dx=abs(x1-x2)
    dy=abs(y1-y2)
    sx=-1
    sy=-1
    if x2>x1:
        sx=1
    if y2>y1:
        sy=1
    error=dx-dy
    while x1!=x2 or y1!=y2:
        image.putpixel((x1,y1),white)
        error_=error
        if error_>-dy:
            error-=dy
            x1+=sx
        if error_<dx:
            error+=dx
            y1+=sy
    image.save("img.bmp")



def Wu(x1,y1,x2,y2,image):
    steep=abs(y2-y1)>abs(x1-x2)
    if steep:
        x1,x2=x2,x1
        y1,y2=y2,y1
    if x1==x2:
        Bresenham(x1,y1,x2,y2,image)
        image.save("Wuline.bmp")
        exit(0)
    if y1==y2:
        Bresenham(x1,y1,x2,y2,image)
        image.save("Wuline.bmp")
        exit(0)
    if (x1>x2):
        x1,x2=x2,x1
        y1,y2=y2,y1
    drawpoint(x1,y1,steep,1,image)
    drawpoint(x2,y2,steep,1,image)
    dx=x2-x1
    dy=y2-y1
    gradient=dy/dx
    x=x1+1
    y=y1+gradient
    while x<=x2-1 or abs(y2-y1)<0.1:
        drawpoint(x,int(y),steep,1-(y-int(y)),image)
        drawpoint(x,int(y)+1,steep,y-int(y),image)
        y+=gradient
        x+=1

    image.save("Wuline.bmp")

image=Image.new("RGBA",(500,500),(0,0,0,255))
Bresenham(10,10,200,100,image)
Wu(100,50,400,400,image)







