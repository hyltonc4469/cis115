#CIS 115
#10.03.18
#M3T2_HyltonMarie

'''
This program creates the star/snowflake drawing using multiple function calls.
This program is also uploaded to my GitHub repository.
'''
#Turtle Python Example:

#Import turtle module
import turtle

def main():
    t=turtle.Turtle()
    sides=int(input("Number of sides?"))
    size=int(input("Size of polygon?"))
    drawPolygon(t, sides, size)
    
    #Initialize 3 instances of turtle.
    j=turtle.Turtle()
    k=turtle.Turtle()
    l=turtle.Turtle()
    
    # Space the turtles:
    j.backward(size*2)
    k.forward(0)
    l.forward(size*2)

    #Customize the Turtles:
    j.pensize=3
    j.pencolor("red")
    k.pensize=4
    k.pencolor("blue")
    l.pensize=5
    l.pencolor("green")

    #Draw Shapes:
    for t in [j, k, l]:
        drawPolygon(t,sides, size)
        
def drawPolygon(t,sides, size):
    angle=360/sides
   
    '''
    uses turtle to draw a nsided polygon.
    input: t- a turtle
    sides-number of sides
    size-length of oe side
    '''
   
    for side in range(sides):    
        t.forward(size)
        t.left(angle)
        
main()
    
    
