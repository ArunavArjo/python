import turtle
turtle.Screen().bgcolor('Blue')
turtle.Screen().setup(300,455)
polygon = turtle.Turtle()

numsides = 6
num_lenth = 88
angle = 360/numsides

for i in range(numsides):
    polygon.forward(num_lenth)
    polygon.right(angle)

turtle.done()