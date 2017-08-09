# https://docs.python.org/3/library/turtle.html
# https://michael0x2a.com/blog/turtle-examples

from turtle import Turtle, done     # import tridy Turtle pro zelvi grafiku
shelly = Turtle()                   # vytvoreni nove zelvy jmenem shelly


# ctverec
# for i in range (4):
#     shelly.forward(200)
#     shelly.right(90)



# polygon
# def polygon(num_sides, side_lenght):
#     angle = 360.0 / num_sides
#     side = side_lenght
#     for i in range(num_sides):
#         shelly.forward(side)
#         shelly.right(-angle)
#     pass
# polygon(3, 150)



# hvezda
# for i in range(5):
#     shelly.forward(150)
#     shelly.right(144)



# hvezda2
for i in range(50):
    shelly.forward(i * 5)
    shelly.right(144)



done()