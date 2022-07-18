#Universidad del Valle de Guatemala
#Graficos por computador - S20 
#Gabriela Paola Contreras Guerra
#SR2 - Lines 

import struct as st
from collections import namedtuple


#Vectors - It just make code more redable 
V2=  namedtuple ('Point2',['x','y'])

#ESPACES THAT I WANT TO USE 
def char (c):
    #1 byte
    return st.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return st.pack ('=h', w)

def dword(d):
    #4 bytes
    return st.pack('=i',d)

# function to set colors 
def color( r,g,b):
    return bytes([int(b*255),
                  int(g*255),
                  int(r*255)]
                )
                    
class Renderer(object):
    
# Define size of the screen 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clearColor =color(0,0,0) # black
        self.currColor = color(1,0,0)
        self.glClear()

#Determinate the background color & array of pixels
    def glClear(self):
        self.pixels = [[ self.clearColor 
                        for y in range(self.height)]  # por cada y en el ancho se le agrega el color definido 
                        for x in range (self.width)]  # por cada x en el largo se le agrega el color definido
    
    def glClearColor(self, r,g,b):
        self.clearColor = color(r,g,b)
    
    def glColor(self, r,g,b):
        self.currColor = color(r,g,b)
    
    # HOW TO MAKE POINTS 
    def glPoint(self, x, y, clr =None):
        if (0 <= x < self.width) and (0<= y < self.height):
            self.pixels[x][y] = clr or self.currColor

#LINES 
    def glLine(self, v0,v1,clr=None):
        #Bresenham line Algorithm
        # y = m*x+b
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0,clr)
            return 

        dy =  abs(y1 - y0)
        dx =  abs(x1 - x0)

        #Inclinacion de una linea 
        steep = dy > dx 

        #Invierto las lineas (Dibujo vertical y no horizontal)
        #Slope is bigger than 1 so I change it 
        if steep:
            x0,y0 = y0,x0
            x1,y1= y1,x1


        #Draw left to right 
        #Initial dot is bigger than final dot I change the values 
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        #Need to redifine because I change the invert the values 
        dy = abs(y1 -y0)
        dx = abs(x1 -x0)

        offset= 0
        limit= 0.5   #Represents the middle of a pixel # Este puede cambiar de acuerdo a nuestras necesidades, pero se recomienda usar .5
        m = dy / dx
        y  = y0 

        for x in range (x0, x1 + 1):
            #Draw de manera vertical 
            if steep:
                self.glPoint(y,x, clr)

            #Draw de manera horizontal 
            else:
                self.glPoint(x,y,clr)
            offset += m 

            if offset >= limit:
                if y0 < y1: #I am going down to up (well the line)
                    y += 1
                else: # The line is been drawing up to down
                    y -= 1
                
                limit += 1

#Function to define image 
    def glFinish(self, filename):
        with open(filename,"wb") as file:
            #HEADER (STEP 1) default BM size(14 bytes)
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            
            #offset 40 bytes + header 14 bytes and color w * h * 3(de bytes)
            file.write(dword( 14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            #INFO HEADER (SETP 2) size(40 bytes)
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))

            #Entre mas color quiera debo de aumentar el bits per pixel 
            file.write(word(24))
            file.write(dword(0)) #compression
            file.write(dword(self.width * self.height * 3)) #size of the screen 
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

        #COLOR TABLE 
            for y in range (self.height):
                for x in range (self.width):
                    file.write(self.pixels[x][y])