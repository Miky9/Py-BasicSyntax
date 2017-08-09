import turtle

# changing line color
# painter = turtle.Turtle()
#
# painter.pencolor("blue")
# for i in range(50):
#     painter.forward(50)
#     painter.left(123)  # Let's go counterclockwise this time
#
# painter.pencolor("red")
# for i in range(50):
#     painter.forward(100)
#     painter.left(123)



# changing line color https://www.webpagefx.com/web-design/color-picker/
# painter2 = turtle.Turtle()
#
# painter2.pencolor("#32D486")
# painter2.forward(90)
#
# painter2.pencolor("#D6305F")
# painter2.forward(90)



# nested loops
# seurat = turtle.Turtle()
#
# dot_distance = 25
# width = 5
# height = 7
#
# seurat.penup()
#
# for y in range(height):
#     for i in range(width):
#         seurat.dot()
#         seurat.forward(dot_distance)
#     seurat.backward(dot_distance * width)
#     seurat.right(90)
#     seurat.forward(dot_distance)
#     seurat.left(90)



# jumping around and changing speed
# The speed cannot be lesser then 0 or greater then 10. 0=warpspeed and will draw as fast as it can
# turtle.setposition(x, y) will set the turtle’s position to the coordinates you plug in. (0, 0) is located at the center of the screen

ninja = turtle.Turtle()

ninja.speed(0)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)


turtle.done()