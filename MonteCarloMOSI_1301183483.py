import math as m
import turtle
from random import randrange, random

# Nama : Muhammad Faishal Darma Putra
# NIM : 1301183483
# Kelas : IF-40-GAB03

# Set Canvas dan Pen untuk menggambar simulasi
canvas = turtle.Screen()
canvas.screensize(250, 250)
canvas.title("Simulasi Monte Carlo untuk mengestimasi nilai phi")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed("fastest")


# meng-set 0 darts yang masuk ke dlm lingkaran(hit)
hit = 0
# banyak darts yang di lemparkan
totalDarts = 100
# Jari jari lingkaran
r = 250

# Gambar Kertas 25x25
pen.color('black')
pen.pu()
pen.setpos(0, 0)
pen.pd()
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)

# Gambar 1/4 lingkaran
pen.color('red')
pen.right(90)
pen.pu()
pen.setposition(250, 0)
pen.pd()
pen.seth(90)
for x in range(90):
    pen.forward(4.33)
    pen.left(1)

# Simulasi
pen.color('green')
pen.pensize(1)
for j in range(totalDarts):
    pen.pu()
    pen.goto(randrange(1,249, 1), randrange(1, 249, 1))
    pen.pd()
    pen.dot()
    x1 = pen.xcor()**2
    y1 = pen.ycor()**2
    if m.sqrt(x1+y1) <= r:      # kondisi apabila true hits akan bertambah 1
      hit += 1


# Outputan
phiEstimasi = (float(hit) / totalDarts) * 4               # Menghitung Estimasi nilai Phi
phiEksak = 3.141592654                                    # Nilai PHIeksak
eror = (phiEstimasi - phiEksak)                           # Menghitung galat erornya

print("Total darts memasuki lingkaran (hits) = " + str(hit))
print("Estimasi nilai phi = " + str(phiEstimasi))
print("Galat eror = " + str(eror))

canvas.exitonclick()
