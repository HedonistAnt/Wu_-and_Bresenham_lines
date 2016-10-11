from PIL import Image
import math
import re
import random
def drawpoint(x,y,s,i,image):
    if s:
        x,y=y,x
    image.putpixel((x,y),(int(255*i),int(255*i),int(255*i),255))
    None
def obj_plotter(filename):
    file=open(filename,"r")
    data=file.read()

    d=re.split(r'[\s /]',data)


    vx=[]
    vy=[]
    vz=[]
    i=-1
    crd=0
    for v in d:         # Vertex
        if v=="vt":
            break
        if v=="v":
            crd=1
            continue
        if crd==1:
            vx.append(v)
            crd=2
            continue
        if crd==2:
            vy.append(v)
            crd=3
            continue
        if crd==3:
            vz.append(v)
            crd=0
    v=''

    crd=0
    vtx=[]
    vty=[]
    vtz=[]
    for v in d: #Texture Vertex
        if v=="vn":
            break;
        if v=="vt":
            crd=1
            continue
        if crd==1:
            vtx.append(v)
            crd=2
            continue
        if crd==2:
            vty.append(v)
            crd=3
            continue
        if crd==3:
            vtz.append(v)
            crd=0
            continue
    crd=0
    vnx=[]
    vny=[]
    vnz=[]
    for v in d:  #Normal Vertex
        if v=="f":
            break;
        if v=="vn":
            crd=1
            continue
        if crd==1:
            vnx.append(v)

            crd=2
            continue
        if crd==2:
            vny.append(v)
            crd=3
            continue
        if crd==3:
            vnz.append(v)
            crd=0
            continue
    f1=[]
    f2=[]
    f3=[]
    ft1=[]
    ft2=[]
    ft3=[]
    fn1=[]
    fn2=[]
    fn3=[]
    crd=0
    for v in d:

        if v=="f":
            crd=1
            continue
        if crd==1:
            f1.append(v)
            crd=2
            continue
        if crd==2:
            ft1.append(v)
            crd=3
            continue
        if crd==3:
            fn1.append(v)
            crd=4
            continue
        if crd==4:
            f2.append(v)
            crd=5
            continue
        if crd==5:
            ft2.append(v)
            crd=6
            continue
        if crd==6:
            fn2.append(v)
            crd=7
            continue
        if crd==7:
            f3.append(v)
            crd=8
            continue
        if crd==8:
            ft3.append(v)
            crd=9
            continue
        if crd==9:
            fn3.append(v)
            crd=0
            continue


    for i in range(len(vx)):
        vx[i]=float(vx[i])
        vy[i]=float(vy[i])
        vz[i]=float(vz[i])
 #   for i in range (len(vtx)):
 #       vtx[i]=float(vtx[i])
  #      vty[i]=float(vty[i])
   #     vtz[i]=float(vtz[i])
  #  for i in range (len(vnx)):
  #      vnx[i]=float(vnx[i])
   #     vny[i]=float(vny[i])
    #    vnz[i]=float(vnz[i])
    for i in range(len(f1)):
      f1[i]=int(f1[i])
      f2[i]=int(f2[i])
      f3[i]=int(f3[i])

      ft1[i]=int(ft2[i])
      ft2[i]=int(ft2[i])
      ft3[i]=int(ft3[i])

      fn1[i]=int(fn1[i])
      fn2[i]=int(fn2[i])
      fn3[i]=int(fn3[i])


    width=int(max(abs(min(vx)),abs(max(vx)))*1000)+500
    height=int(max(abs(min(vy)),abs(max(vy)))*1000)+500

    image=Image.new("RGBA",(width,height),(0,0,0,255))
    print("max f1=",max(f1))
    print("max f2=",max(f2))
    print("max f3=",max(f3))
    print("len(vx)=",len(vx))
    print("len(vy)=",len(vy))
    print("min f1=",min(f1))
    scaling=min(width,height)/2
    for i in range(len(f1)):
        Ax=round(vx[f1[i]-1]*scaling+(width)/2)
        Ay=round(vy[f1[i]-1]*scaling+(height)/2)
        Bx=round(vx[f2[i]-1]*scaling+(width)/2)
        By=round(vy[f2[i]-1]*scaling+(height)/2)
        Cx=round(vx[f3[i]-1]*scaling+(width)/2)
        Cy=round(vy[f3[i]-1]*scaling+(height)/2)

        """"
        R=random.randrange(0, 255, 1)

        G=random.randrange(0, 255, 1)

        B=random.randrange(0, 255, 1)

        points=dict()
        a=dict()
        b=dict()
        c=dict()
        a=foreach(Ax,Ay,Bx,By,points)
        b=foreach(Ax,Ay,Cx,Cy,a)
        c=foreach(Bx,By,Cx,Cy,b)
        fill_str(c,image,(R,G,B,255),"img.bmp")
        """""

        Bresenham(Ax,Ay,Bx,By,(255,255,255,255),image)
        Bresenham(Ax,Ay,Cx,Cy,(255,255,255,255),image)
        Bresenham(Bx,By,Cx,Cy,(255,255,255,255),image)







def Bresenham(x1,y1,x2,y2,color,image):
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
        image.putpixel((x1,y1),color)
        error_=error
        if error_>-dy:
            error-=dy
            x1+=sx
        if error_<dx:
            error+=dx
            y1+=sy

    image.save("img.bmp")

def Wu(x1,y1,x2,y2,image,color,filename):
    s=abs(y2-y1)>abs(x1-x2)
    if s:
        x1,x2=x2,x1
        y1,y2=y2,y1
    if x1==x2:
        Bresenham(x1,y1,x2,y2,color,image)

        return
    if y1==y2:
        Bresenham(x1,y1,x2,y2,color,image)

        return
    if (x1>x2):
        x1,x2=x2,x1
        y1,y2=y2,y1
    drawpoint(x1,y1,s,1,image)
    drawpoint(x2,y2,s,1,image)
    dx=x2-x1
    dy=y2-y1
    gradient=dy/dx
    x=x1+1
    y=y1+gradient
    while x<=x2-1 or abs(y2-y1)<0.1:
        drawpoint(x,int(y),s,1-(y-int(y)),image)
        drawpoint(x,int(y)+1,s,y-int(y),image)
        y+=gradient
        x+=1

    image.save(filename)

def foreach(x1,y1,x2,y2,points):
    if y1>y2:
        y1,y2=y2,y1
        x1,x2=x2,x1
    y=math.ceil(y1)
    if y2-y1==0:
     return points
    dx=(x2-x1)/(y2-y1);#!!!!!!!
    x=x1+dx*(y-y1)
   # points={y:[]}

    while (y+1<=y2):
        if(y not in points.keys()):
            points[y] = [];
        points[y].append(x)

        y+=1
        x+=dx
    return points

def fill_str(d,image,color,filename):



    l=d.keys()
    for y in l:
      s=d.get(y)
      s.sort()
      for i in range(len(s)-1):
        x=s[i]
        while(x<=s[i+1]):
          image.putpixel((int(x),y),color)
          x+=1
    image.save(filename)


def fill_seed(pix,color1,color2,image,filename):
    stack=list()
    stack.append(pix)
    while (len(stack)!=0):
        pix=stack.pop()

        if (image.getpixel((pix[0],pix[1]))!=color1)and (image.getpixel((pix[0],pix[1]))!=color2):
          image.putpixel((pix[0],pix[1]),color2)

        if (image.getpixel((pix[0]+1,pix[1]))!=color1 and image.getpixel((pix[0]+1,pix[1]))!=color2):
            newpix=[pix[0]+1,pix[1]]
            stack.append(newpix)
        if (image.getpixel((pix[0]-1,pix[1]))!=color1 and image.getpixel((pix[0]-1,pix[1]))!=color2):
            newpix=[pix[0]-1,pix[1]]
            stack.append(newpix)
        if (image.getpixel((pix[0],pix[1]+1))!=color1 and image.getpixel((pix[0],pix[1]+1))!=color2):
            newpix=[pix[0],pix[1]+1]
            stack.append(newpix)
        if (image.getpixel((pix[0],pix[1]-1))!=color1 and image.getpixel((pix[0],pix[1]-1))!=color2):
            newpix=[pix[0],pix[1]-1]
            stack.append(newpix)
    image.save(filename)
def vcode(x,y,rx_max,ry_max,rx_min,ry_min):
    LEFT=1
    RIGHT=2
    BOT=4
    TOP=8
    code=0
    if x<rx_min:
       code=code+LEFT
    if x>rx_max:
        code=code+RIGHT
    if y<ry_min:
        code=code+BOT
    if y>ry_max:
        code=code+TOP
    return(code)



def cohen_sutherland(x1,y1,x2,y2,rx_max,ry_max,rx_min,ry_min):
   code_a=vcode(x1,y1,rx_max,ry_max,rx_min,ry_min)
   code_b=vcode(x2,y2,rx_max,ry_max,rx_min,ry_min)
   LEFT=1
   RIGHT=2
   BOT=4
   TOP=8
   while (code_a | code_b):
    if code_a & code_b:
        return [False]
    if (code_a):
        code=code_a
        c=[x1,y1]
    else:
        code=code_b
        c=[x2,y2]
    if (code&LEFT):
        c[1]+=(y1-y2)*(rx_min-c[0])/(x1-x2)
        c[0]=rx_min
    elif (code&RIGHT):
        c[1]+=(y1-y2)*(rx_max-c[0])/(x1-x2)
        c[0]=rx_max
    elif(code&BOT):
        c[0]+=(x1-x2)*(ry_min-c[1])/(y1-y2)
        c[1]=ry_min
    elif(code&TOP):
        c[0]+=(x1-x2)*(ry_max-c[1])/(y1-y2)
        c[1]=ry_max
    if(code==code_a):
        x1=c[0]
        y1=c[1]
        code_a=vcode(x1,y1,rx_max,ry_max,rx_min,ry_min)
    else:
        x2=c[0]
        y2=c[1]
        code_b=vcode(x2,y2,rx_max,ry_max,rx_min,ry_min)

   return [True,x1,y1,x2,y2]

def liang_barski (x1,y1,x2,y2,left,right,bot,top):
    t0=0.0
    t1=1.0
    dx=x2-x1
    dy=y2-y1
    edge=0
    while edge<4:
        if (edge==0):
            p = -dx
            q = -(left-x1)
        if (edge==1):
            p = dx
            q =  (right-x1)
        if (edge==2):
            p = -dy
            q = -(bot-y1)
        if (edge==3):
            p = dy
            q =  (top-y1)
        if p!=0:
          r=q/p

        if (p==0) and (q<0):
             return [False]
        if(p<0):
            if(r>t1):
                return [False]
            elif(r>t0):
                t0=r
        elif(p>0):
            if(r<t0):
               return [False]
            elif(r<t1):
               t1=r
        edge+=1
    nx1 = x1 + t0*dx
    ny1 = y1 + t0*dy
    nx2 = x1 + t1*dx
    ny2 = y1 + t1*dy
    return [True,nx1,ny1,nx2,ny2]







