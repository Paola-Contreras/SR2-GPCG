#Universidad del Valle de Guatemala
#Graficos por computador - S20 
#Gabriela Paola Contreras Guerra
#SR2 - Lines 


from lines import Renderer, color, V2

w = 1900
h = 450

#Size of my screen 
rend = Renderer(w,h)

# TRIANGLE 

rend.glLine(V2(90,110), V2(300,110))
rend.glLine(V2(88,113), V2(200,350))
rend.glLine(V2(200,350),V2(300,113))


# SQUARE 

rend.glLine(V2(400,110), V2(400,340), color(0,1,0))
rend.glLine(V2(650,340), V2(400,340), color(0,1,0))
rend.glLine(V2(650,110), V2(650,340), color(0,1,0))
rend.glLine(V2(400,110), V2(650,110), color(0,1,0))

#Hexagon
rend.glLine(V2(800,340), V2(975,340), color(1,1,1))
rend.glLine(V2(800,99), V2(975,99), color(1,1,1))
rend.glLine(V2(750,220), V2(800,100), color(1,1,1))
rend.glLine(V2(975,100), V2(1030,220), color(1,1,1))
rend.glLine(V2(975,340), V2(1030,220), color(1,1,1))
rend.glLine(V2(800,340), V2(750,220), color(1,1,1))

#Pentagon
rend.glLine(V2(1160,110), V2(1350,110), color(1,0,1))
rend.glLine(V2(1250,355), V2(1100,260), color(1,0,1))
rend.glLine(V2(1250,355), V2(1400,260), color(1,0,1))
rend.glLine(V2(1100,260), V2(1160,110), color(1,0,1))
rend.glLine(V2(1400,260), V2(1350,110), color(1,0,1))

#Diamond
rend.glLine(V2(1650,365), V2(1500,230), color(1,1,0))
rend.glLine(V2(1650,365), V2(1800,230), color(1,1,0))
rend.glLine(V2(1650,95), V2(1500,230), color(1,1,0))
rend.glLine(V2(1650,95), V2(1800,230), color(1,1,0))

#GENEATE IMG 
rend.glFinish("output2.bmp")