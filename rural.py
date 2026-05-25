#ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY
#COMPUTER SCIENCE, INTRODUCTION TO PYTHON
#GROUP ASSIGNMENT
#TITLE: RURAL VILLAGE, CS1GRAPHICS
#!the animation may not start quickly!





from cs1graphics import*
village=Canvas(1000,600,"skyBlue","Rural Village")
def rects(a,b,e,f,g,i,j,l):
    rect=Rectangle(a,b)
    rect.setBorderColor(e)
    rect.setFillColor(f)
    rect.setDepth(g)
    rect.moveTo(i,j)
    rect.setBorderWidth(1)
    l.add(rect)
def trgls(a,b,c,d,x,y,e,f,g,i,j,l):
    trgl=Polygon(Point(a,b),Point(c,d),Point(x,y))
    trgl.setBorderColor(e)
    trgl.setFillColor(f)
    trgl.setDepth(g)
    trgl.moveTo(i,j)
    l.add(trgl)
def crcls(a,b,c,d,e,f,l):
    crcl=Circle(a)
    crcl.setBorderColor(b)
    crcl.setFillColor(c)
    crcl.setDepth(d)
    crcl.moveTo(e,f)
    l.add(crcl)
def legs(a,b,c,d,e,f,g,h,i,j,n,l):
    for r in range(2):
        pth=Path(Point(a,b),Point(c,d))
        pth.setBorderColor(e)
        pth.setBorderWidth(f)
        pth.setDepth(g)
        pth.rotate(h)
        pth.moveTo(i+n*r,j)
        l.add(pth)
def zigzags(a,b,c,d,e,f,x,y,g,h,k,m,n,i,j,l):
    zig=Path(Point(a,b),Point(c,d),Point(e,f),Point(x,y))
    zig.setBorderColor(g)
    zig.setDepth(h)
    zig.setBorderWidth(k)
    zig.scale(m)
    zig.rotate(n)
    zig.moveTo(i,j)
    l.add(zig)
def walls(a,b,c,d,e,f,x,y,g,h,l):
    wall=Polygon(Point(a,b),Point(c,d),Point(e,f),Point(x,y))
    wall.setFillColor(g)
    wall.setDepth(h)
    l.add(wall)
def noses(a,b,c,d,e,f,x,y,g,h,i,j,l):
    nose=Polygon(Point(a,b),Point(c,d),Point(e,f),Point(x,y))
    nose.setFillColor(g)
    nose.setDepth(h)
    nose.scale(2)
    nose.moveTo(i,j)
    l.add(nose)
#Sun
sun2 = Circle()
village.add(sun2)
sun2.setRadius(25)
sun2.setFillColor("yellow")
sun2.setDepth(90)
sun2.setBorderColor("yellow")
sun2.moveTo(30, 299)

#Humans
human=Layer()
crcls(10,"black","brown",50,400,500,human)
legs(500,300,500,340,"black",7,60,0,385,511.5,32,human)
legs(500,300,500,340,"black",8.5,60,0,394,557,13,human)
rects(24,45,"black","dark blue",50,400,534,human)
human.move(515,103)
human.scale(0.8)
village.add(human)

human1=Layer()
crcls(10,"black","brown",50,400,500,human1)
legs(500,300,500,340,"black",7,60,0,385,511.5,32,human1)
legs(500,300,500,340,"black",8.5,60,0,394,557,13,human1)
rects(24,45,"black","purple",50,400,534,human1)
human1.scale(0.8)
human1.move(480,103)
village.add(human1)


#Cattles
catl=Layer()
noses(497,297,500,300,510,297,507,287,(130,130,130),50,330,470,catl)
rects(65,25,"black",(160,160,160),50,385,461.5,catl)
crcl=Circle(10)
crcl.setFillColor("black")
crcl.moveTo(388,461.5)
catl.add(crcl)
legs(500,300,500,320,"black",17,50,60,380,456.5,32,catl)
legs(500,300,500,325,"black",6,60,0,370,470,40,catl)
legs(500,300,500,325,"black",6,60,0,360,470,40,catl)
legs(500,300,500,310,"black",2,50,7,348,443,4,catl)
zigzags(-20,-15,0,0,15,-10,15,-10,"black",50,2,1,1,415,450,catl)
catl.setDepth(60)
village.add(catl)

catl2=catl.clone()
catl2.move(178,-107)
village.add(catl2)

catl3=catl.clone()
catl3.move(30,-87)
catl3.rotate(3)
village.add(catl3)

catl4=catl.clone()
catl4.move(168,70)
village.add(catl4)

catl5=catl.clone()
catl5.move(-168,-100)
village.add(catl5)

#Trees
tree=Layer()
crcls(30,"black",(0,75,0),50,500,300,tree)
rects(7,20,"black","brown",30,500,337,tree)
village.add(tree)
tree.setDepth(60)

tree3=Layer()
tree1=tree.clone()
tree1.move(-60,15)
tree1.scale(1.4)
tree3.add(tree1)
village.add(tree3)
tree3.setDepth(46)

tree2=tree.clone()
tree2.move(-400,15)
village.add(tree2)

#A hut
hut=Layer()
trgls(700,300,590,420,810,420,"black",(100,45,0),40,700,280,hut)
rects(180,100,"black",(100,45,0),70,700,450,hut)
rects(40,65,"black","black",60,680,467.5,hut)
rects(30,30,"black","black",60,725,440,hut)
hut.setDepth(40)
hut.move(150,80)
village.add(hut)

#Mountains
mountain=Layer()
trgls(500,400,250,500,750,500,"black",(85,40,0),80,600,100,mountain)
mountain.setDepth(80)
village.add(mountain)
mountain.moveTo(200,100)
mountain.move(70,0)

mountain1=mountain.clone()
mountain1.setDepth(90)
village.add(mountain1)
mountain1.moveTo(-100,100)

mountain2=mountain.clone()
village.add(mountain2)
mountain2.moveTo(-400,100)

#A barn
barn=Layer()
walls(340,270,292,306,492,306,540,270,(120,120,120),60,barn)
walls(300,300,300,400,500,400,500,300,"brown",70,barn)
walls(500,300,500,400,540,360,540,270,"brown",70,barn)
walls(350,400,450,400,450,350,350,350,"black",60,barn)
barn.setDepth(70)
village.add(barn)
barn.move(450,-20)

#Ground
land=Layer()
rects(1000,300,"green","dark green",80,500,450,land)
land.setDepth(80)
#River
flow=Layer()
river=Spline(Point(400,620),Point(150,510),Point(-10,500))
river.setBorderColor((0,200,200))
river.setBorderWidth(100)
river.setDepth(60)
river.move(-10,30)
river.rotate(5)
flow.add(river)
#river flows
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,0,480,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,0,500,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,0,520,flow)

zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,130,500,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,130,520,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,120,540,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,110,560,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,180,540,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,180,580,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,180,530,flow)

zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,30,470,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,30,490,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,50,515,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,10,530,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,80,510,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,80,550,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,80,490,flow)

zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,230,540,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,230,560,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,220,580,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,210,600,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,280,590,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,280,610,flow)
zigzags(0,50,50,0,100,50,150,0,"light blue",50,2,0.5,30,280,570,flow)
land.add(flow)
village.add(land)

#Birds
birds=Layer()
bird=Path(Point(0,0),Point(5,0),Point(7.5,4.3),Point(10,0),Point(15,0))
bird.setBorderColor("black")
bird.setDepth(20)
bird.setBorderWidth(1.5)
bird.moveTo(750,50)
bird.scale(2)
birds.add(bird)

bird1=bird.clone()
bird1.moveTo(815,50)
birds.add(bird1)

bird2=bird.clone()
bird2.moveTo(775,70)
birds.add(bird2)
village.add(birds)
birds.moveTo(250,60)


#ANIMATION

from math import*

def animate_set(sun2):
     w = 1000
     h = 600
     r = 25
     x0 = w / 2.0
     y0 = h + r+5
     max_x  =1500.0/ 2.0 - r+5
     max_y  = 600.0
     for i in range(20000):
         if i<14000:
             continue
         else:
             rad = (i/22000.0) * pi
             x = x0 - (max_x * cos(rad))
             y = y0 - (max_y * sin(rad))
             sun2.moveTo(50+x, y+50)

def late(sun2):
     w = 1000
     h = 600
     r = 25
     x0 = w / 2.0
     y0 = h + r+5
     max_x  =1500.0/ 2.0 - r+5
     max_y  = 600.0
     for i in range(20000):
         if i<7000:
             continue
         elif i==14000:
             break
         else:
             rad = (i/22000.0) * pi
             x = x0 - (max_x * cos(rad))
             y = y0 - (max_y * sin(rad))
             sun2.moveTo(50+x, y+50)

def animate_rise(sun2):
     w = 1000
     h = 600
     r = 25
     x0 = w / 2.0
     y0 = h + r+5
     max_x  =1500.0/ 2.0 - r+5
     max_y  = 600.0
     for i in range(20000):
         if i==7000:
             break
         else:
             rad = (i/22000.0) * pi
             x = x0 - (max_x * cos(rad))
             y = y0 - (max_y * sin(rad))
             sun2.moveTo(50+x, y+50)

catl.moveTo(480,-105)
catl4.moveTo(430,-110)
catl2.moveTo(470,-107)
catl3.moveTo(450,-110)
catl5.moveTo(500,-110)

catl.setDepth(90)
catl2.setDepth(90)
catl3.setDepth(90)
catl4.setDepth(90)
catl5.setDepth(90)

animate_rise(sun2)


human.setDepth(20)
human1.setDepth(20)

for i in range (50):
    human.move(-1,1)
    human1.move(-1,1)
    human.setDepth(40)
    human1.setDepth(40)
for i in range (100):
    human.move(-1,-1)
    human1.move(-1,-1)
for i in range (250):
    human.setDepth(50)
    human.move(0.9,-0.5)
    human1.move(-0.5,-0.25)
human.move(20,0)

catl.setDepth(50)
for i in range (50):
    catl.move(-1,1)
catl2.setDepth(50)
for i in range (50):
    catl2.move(-1,1)
catl3.setDepth(50)
for i in range (50):
    catl3.move(-1,1)
catl4.setDepth(50)
for i in range (50):
    catl4.move(-1,1)
catl5.setDepth(50)
for i in range (50):
    catl5.move(-1,1)
    
for i in range (500):
    catl2.move(-1.49,0)
    catl3.move(-0.8,(i/435)*2)
    catl4.move(-1.2,0.1)
for i in range (250):
    catl.move(-2,-0.35)
    catl5.move(-1,-0.25)
for i in range (500):
    human.move(-0.8,0.35)
    human.setDepth(40)
for i in range (500):
    catl3.move(-0.1,-0.3)

for i in range (1000):
    birds.move(-0.5,0.00017*i)
    birds.move(-0.5,0.00017*i)
    birds.move(-0.5,0.1)
    human.move(-0.8/5,-0.35/3)
human.setDepth(48)
human1.setDepth(50)

late(sun2)

for i in range (1000):
    human1.move(-0.09,-0.15)
    human.move(0.55,-0.05)

for i in range (500):
    catl2.move(1.49,0)
    if i <300:
        catl3.move(0.8,-(i/435)*2)
    catl4.move(1.2,-0.1)
catl5.setDepth(52)
for i in range (250):
    catl.move(2,0.35)
    catl5.move(1,0.25)
    catl3.move(0.8,0)
    
for i in range (600):
    catl2.move(0.04,-0.09)
    catl5.move(0.04,-0.09)
    catl.move(0.04,-0.09)
catl.setDepth(90)
catl2.setDepth(90)
catl5.setDepth(90)
for i in range (600):
    catl4.move(0.15,-0.09)
    catl3.move(0.15,-0.09)
catl4.setDepth(90)
catl3.setDepth(90)

human.setDepth(45)
human1.setDepth(45)
for i in range (500):
    human.move(-0.8,0.35)
    human1.move(0.1,0.54)
human.setDepth(30)
human1.setDepth(30)
for i in range (500):
    human.move(0.6,0)
    human1.move(0.6,0)

for i in range (50):
    human.move(0.3,0.01)
human.setDepth(90)
for i in range (50):
    human1.move(0.5,0.01)
human1.setDepth(90)
    
animate_set(sun2)
































