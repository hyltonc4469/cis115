#CIS 115
#Oct. 8
#Hylton Marie


import turtle
def main():
    t=turtle.Turtle()
    sides=int(input("Number of sides: "))
    size=int(input("Size of polygon: "))
    drawPolygon(t, sides, size)
    
    
def drawPolygon(t, sides, size):
    angle=360/sides
    for side in range(sides):
        
        t.forward(size)
        drawTriangle(t, sides, size)
        t.left(angle)
       # drawTriangle(t, sides, sides) 

def drawTriangle(t, size,sides):
    angle=360/3
    for i in range(3):
        
        t.backward(size)
        t.right(angle)
        
   


main()







