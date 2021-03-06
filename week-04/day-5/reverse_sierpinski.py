# Reverse Sierpinski triangle
# Triangles are equilateral, so triangle height (h) is:
# a * sqr(0,75), or a * 0,866

from tkinter import *

root = Tk()
w = 667
h = 0.866
canvas = Canvas(root, width=w, height=w*h, bg="lightgray")
canvas.pack()

def draw_eq_triangle(x, y, a):

    topleft = x, y
    topright = x + a, y
    bottom = x + (1/2 * a), y + (a * h)

    canvas.create_polygon(topleft, topright, bottom, fill='white', outline='black')

def reverse_sierpinski(x, y, a, depth):
    draw_eq_triangle(x, y, a)
    if a > depth:
        reverse_sierpinski(x, y, a/2, depth)
        reverse_sierpinski(x + a/2, y, a/2, depth)
        reverse_sierpinski(x + a/4, y + a/2 * h, a/2, depth)

reverse_sierpinski(30, 10, 600, 10)

root.mainloop()
