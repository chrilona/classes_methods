# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

from cmath import pi


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def circle_area(self):
        area = pi*self.radius*self.radius
        print(f"Your circle area is {area}")

    def circle_perimeter(self):
        circum=pi*(self.radius+self.radius)
        print(f"The circumference of this circle is {circum}")


# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,a):
          self.a = a
    def square_area(self):
        area_square=self.a*self.a
        print(f"Your squares total area is {area_square}")
    def square_perimeter(self):
        perimeter=self.a+self.a+self.a+self.a
        print(f"Your square's perimeter is {perimeter}")


# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area_rectangle(self):
        area_rect=self.w*self.l
        print(f"The area of this rectangle {area_rect}")
    def perimeter_rectangle(self):
        perimeter_rect=2(self.l+self.w)
        print(f"The perimeter of this rectangle is {perimeter_rect} ")

# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,rad):
        self.rad = rad
    def surface_area(self):
        sphere_area = 4*pi*(self.rad*self.rad)
        print(f"Your sphere's surface area is { sphere_area} ")
    def sphere_volume(self):
        sphere_vol = 4/3*pi(self.rad**3)
        print(f"Your sphere's volume is {sphere_vol}")
        

        



        
