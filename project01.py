# project01.py, Sai Kathika
#import basicShapes
import random
from basicShapes import *
if __name__=="__main__":
    print('Inside main of project01.py')

def drawTree(height, color):

      stem = (height)/3
      treeWidth = (0.5 * height)
        


      t.up()
      t.forward(0.4*(treeWidth))
      t.down()
      drawRectangle(0.2 * (treeWidth), stem, 0, 'brown', 'brown') 

      t.up()
      t.backward(0.4*(treeWidth))
      t.left(90)
      t.forward(stem)
      t.right(90)
      t.down()
      drawTriangle(treeWidth, stem, color, (color)) 

      t.up()
      t.left(90)
      t.forward(0.5*stem)
      t.right(90)
      t.down()
      drawTriangle(treeWidth, stem, (color), (color)) 

      t.up()
      t.left(90)
      t.forward(0.5*stem)
      t.right(90)
      t.down()
      drawTriangle(treeWidth, stem, (color), (color)) 

                                                                                      #Return to Original Position        
      t.right(90)
      t.up()
      t.forward((2/3)*height)
      t.left(90)
      t.down

        

def drawForest(n):
    n=int(n)
    for i in range (n):

        t.seth(0)
        t.up()
        x=random.randint(-650,650) 
        y=random.randint(-200,180)
        t.goto(x,y)  
        t.down()
        shadesOfGreen =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]
        color = random.choice(shadesOfGreen)
        x=random.randint(100,250)
        drawTree(x,color)
##        x1 = t.xcor()
##        y1 = t.ycor()
##        t.goto(x1,y1)

        
def checkTreeHeight():
    t.up()
    t.goto(0,-200)
    t.down()
    drawRectangle(200, 200, 0 , "red","")
    t.seth(0)
    drawTree(200, "green")

    
def drawHut():
    x1 = t.xcor()
    y1 = t.ycor()

    for i in range(10):
        drawRectangle(15,80,0,"black","brown")
        t.forward(9)
        t.down()
   
    t.up()
    t.goto(x1+40,y1+110)
    t.down()
    for i in range(45):
        x=random.randint(65,80)
        y=random.randint(115,260)
        drawRectangle(10,x,y,"black","brown")
        t.up()
        t.goto(x1+45,y1+110)
        t.down()
        
def drawVillage(v):
    n=int(v)
    for i in range(v):
        t.seth(0)
        t.up()
        x=random.randint(-600,600)
        y=random.randint(-350,-250)
        t.goto(x,y)
        t.down()
        drawHut()

def drawGrass():
##        t.up()
##        t.goto(0,0)
##        t.down()
        drawRectangle(5,60,300,"green","green")
    
def drawMeadow():
    for i in range(150):
        t.seth(0)
        t.up()
        x=random.randint(-700,700)
        y=random.randint(-350,-300)
        t.goto(x,y)
        drawGrass()

def drawSun():
    t.up()
    t.goto(0,170)
    t.down()
    t.color('yellow')
    t.begin_fill()
    t.circle(75)
    t.end_fill()
    t.up()
    t.goto(0,245)
    count=1
    for i in range(65):
        count=(count*5)+90
        drawRectangle(5,165,count,'yellow','yellow')
##    drawRectangle(5,165,95,'yellow','yellow')
##    drawRectangle(5,165,100,'yellow','yellow')

def drawSky():
    t.up()
    t.goto(-700,70)
    drawRectangle(90000,5000,0,'light blue','light blue')

def drawScene(n,v):
##    t.up()
##    t.goto(0,170)
##    t.down()
    drawSky()
    drawForest(n)
    drawSun()
    drawMeadow()
    drawVillage(v)






    
