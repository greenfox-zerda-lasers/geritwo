# Hexagonal fractal 2: 3 hexagons inside

from tkinter import *

root = Tk()
w = 696 # height = 545
h = 0.866
canvas = Canvas(root, width=w, height=545, bg="lightgray")
canvas.pack()

def draw_hexagon(x, y, a):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill='white', outline='black')

def hexagonal_fractal(x, y, a, depth):
    draw_hexagon(x, y, a)
    if a > depth:
        a = a/2
        hexagonal_fractal(x, y, a, depth)
        hexagonal_fractal(x + (1.5 * a), y + (a * h), a, depth)
        hexagonal_fractal(x, y + 2 * (a * h), a, depth)
hexagonal_fractal(200, 10, 300, 10)

root.mainloop()
