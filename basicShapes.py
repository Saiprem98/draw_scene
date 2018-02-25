'''
Sai Kathika
Lab 03
'''

import turtle
import math

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.width(4)
if __name__=="__main__":
    t.color("green", "yellow")

def drawRectangle_1():
      
     #   draw a rectangle with width 50 and height 100. Use a turtle called t to create the drawing
        
        t.seth(0)       # Set the initial orientation of the turtle to 0 degrees
        t.begin_fill()
        t.forward(50)    # Move the turtle forward by 50 units in the direction that it was pointing
        t.left(90)       # Turn the turtle left by 90 degrees relative to the direction it was pointing
        t.forward(100)   # Move the turtle forward by 100 units
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)       # Make sure the turtle is oriented back to its initial orientation
        t.end_fill()
def drawRectangle_2():
        
     #   draw a rectangle with width 50, height 100, tilt 0, pen color green and fill color yellow . Use a turtle called t to create the drawing
        

        # Calculate the coordinates for the four corners of the rectangle

        x1 = t.xcor()
        y1 = t.ycor()

        x2 = x1 + 50
        y2 = y1

        x3 = x2
        y3 = y2 + 100

        x4 = x1
        y4 = y1 + 100

        
        t.color("green", "yellow") # set the pen and fill colors
        t.begin_fill()
        
        # Command the turtle to visit the four corners in order
        t.goto(x2, y2)
        t.goto(x3, y3)
        t.goto(x4, y4)
        t.goto(x1, y1)
        
        t.end_fill()
def drawRectangle_3():
        
     #   draw a rectangle with width 50, height 100, tilt 0, pen color green and fill color yellow . Use a turtle called t to create the drawing
        

        # Calculate the coordinates for the four corners of the rectangle

        x1 = t.xcor()
        y1 = t.ycor()

        fourCorners = [(x1 + 50, y1), (x1 + 50, y1 + 100), (x1, y1 + 100), (x1, y1)]
        
        t.color("green", "yellow")
        t.begin_fill()
        
        t.goto(fourCorners[0][0], fourCorners[0][1])
        t.goto(fourCorners[1][0], fourCorners[1][1])
        t.goto(fourCorners[2][0], fourCorners[2][1])
        t.goto(fourCorners[3][0], fourCorners[3][1])

        t.end_fill()

def drawRectangle(width,height,tilt,penColor,fillColor):
        t.color(penColor,fillColor)
        t.seth(tilt)       
        t.begin_fill()
        t.forward(width)    
        t.left(90)       
        t.forward(height)   
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)       
        t.end_fill()
def drawTwoRectangles():
        drawRectangle( 50, 100, 0, "red", "") 

        t.seth(0)   # Set the absolute heading of the turtle to 0 degrees (pointing east)


        # Move the turtle right by 200 units without leaving a trail 
        t.up()     
        t.forward(100)  
        t.down()

#        drawRectangle( 100, 150, 22, "green", "yellow") 
       

#drawTwoRectangles()  

def drawTriangle(base,height,penColor,fillColor):
        """
        draw a triangle with a given base, height, penColor and fillColor,
        with the current location of the turtle being the 
        lower left corner. The base of the triangle should be at 0 degrees with respect to the x-axis. 
        Do not assume anything about the initial orientation of the turtle. 
        The final orientation of the turtle should be 0 degrees with respect to the x-axis. 
        Use a turtle called t to create the drawing
        """
        leg=math.sqrt(((base/2)**2)+(height**2))
        angle=(math.degrees((math.atan((height)/(base/2)))))
        topAngle=2*angle
        t.color(penColor,fillColor)
        t.seth(0)
        t.begin_fill()
        t.forward(base)
        t.left(180-angle)
        t.forward(leg)
        t.left(topAngle)
        t.forward(leg)
        t.seth(0)

        t.end_fill()
    # drawTriangle(100,80,"blue","red")

def drawTwoTriangle():
        """ Draws two non overlapping triangles with different sizes and colors
        """
        t.up()
        t.forward(200)
        t.down()
        drawTriangle(100,80,"blue","red")
        t.seth(0)

        t.up()
        t.forward(250)
        t.down()

#        drawTriangle(50,85,"green","yellow")

#drawTwoTriangle()

