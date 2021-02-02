import graphics.rectangle
print("Rectangle")
l=int (input("Enter length:"))
b=int(input("Enter breadth:"))
print("Area=",graphics.rectangle.area(l,b))
print("Perimeter=",graphics.rectangle.perimeter(l,b))
print()
from graphics.circle import area
from graphics.circle import perimeter as p
print("Circle")
r=int(input("Enter radius:"))
print("Area=",area(r))
print("perimeter=",p(r))
print()
from graphics.degraphics.cuboid import area as a
from graphics.degraphics.cuboid import perimeter as p
print("Cuboid")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
h=int(input("Enter height"))
print("Area=",a(l,b,h))
print("Perimeter",p(l,b,h))
print()
from graphics.degraphics.sphere import *
print("Sphere")
r=int(input("Enter radius"))
print("Area=",area(r))
print("Circumference=",circumference(r))
      


