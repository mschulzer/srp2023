from turtle import *
import time
import numpy as np
import math


###################################################################
# Definér nogle funktioner
###################################################################

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

def vind(x):
    f = 2
    s = 200
    x = np.arange(s)
    y = np.sin(2 * np.pi * f * x/s)
    return y

# Magnus-effekten: r*V*((2*pi*r)^2)*w*L
def magnus(v):
    return ((math.pow((2*math.pi*2.5), 2))*1.225*30*1*v)

def newton_kg(x):
    return (x*0.1019716)

###################################################################
# Sæt nogle variabler - og initiér Turtle()
###################################################################

t = Turtle()
setup(800, 500)
bgcolor("lightskyblue")


""" Main """
for i in range(100):
    t.forward(8)
    if (i % 4 == 0):
        t.right(math.sin(i)*10)
        
    eraseble = erasableWrite(t, magnus(i), font=("Arial", 20, "normal"), align="center")
    
    time.sleep(1)
    eraseble.clear()
