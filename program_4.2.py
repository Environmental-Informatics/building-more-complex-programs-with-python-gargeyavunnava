
"""
Created on Fri Jan 24 13:50:40 2020
Purdue account name: vvunnava
Github account name: gargeyavunnava
Exercise 4.2, thinkpython 2e

Program description:
Multiple functions are defined to make it easy to draw the three flowers
as shown in fig 4.1, thinkpython 2e
    
As discussed in the chapter, a 'polyline' funtion is defined here to make it 
easier compared  to a polygon function to draw geometrical shapes. 

The polyline function defined is then used in the definition of another 
function 'arc' to help draw arcs.

"""

import turtle #to work with turtle
import math  #to use math constants like pi

"""
polyline function: it takes 4 inputs: t=turtle object, n = no of lines/sides,
length and angle.The polyline is created using a for loop where in each iteration
the trutle moves forward as directed by the length variable value and then turns
at an angle as directed by angle variable. The next iteration of for loop begins
at the end location of the turtle in the previous iteration and this creates a
continous polyline.
"""

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
"""
arc function: it takes 3 inputs: t=turtle object, r=radius, and angle= angle of 
the arc (ex: angle=360 - circle, angle=90 - semicircle).
arc length is calculated by the formula 2*pi*r, pi value from the math function
The arc circumference is approximated as using a many sided (variable n) polyline. 
More the sides, smoother the curve. Once n is determined, n is used to calculate 
the individual polyline's length and turning angle 
"""   
def arc(t,r,angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t,n,step_length,step_angle)
    
def circle(t,r):  # an arc with a fixed angle = 360
    arc(t,r,360)

"""
petal function: takes 3 inputs: t=turtle object, r =radius and angle
the function calls the arc function twice in a for loop to create the shape of 
a petal. After the 1st iteration, turtle is turned by an angle of (180-angle)
to create the petal shape.
"""
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)  #turn angle
"""
flower function: takes 4 inputs: t=turtle object, r=radius, angle and n=no of 
petals in the flower. To create the shape of a flower with n petals, the function 
calls the petal function n times in a loop. The way the petals are arranged is
modifed the the angle variable.
"""        

def flower(t,r,angle,n):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)  #arranging multiple petals 

"""
offset function is defined to moce the turtle in the turtle window.
pu = pen up, turtle moving path not displayed
pd = pen down, turtle moving path displayed.
"""

def offset(t, offset_length):  #moving turtle position
    t.pu()
    t.fd(offset_length)
    t.pd()

bob=turtle.Turtle()

offset(bob,-200)
flower(bob,80,60,6)


offset(bob,200)
flower(bob,60,80,10)

offset(bob,200)
flower(bob,180,15,20)

"""
reset function used to keep the turtle window open and modify the code without the
need to restart the kernel
"""
#bob.reset() 

turtle.mainloop()



