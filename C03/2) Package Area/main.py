from graphics import circle,rectangle
from graphics.threedgraphics import cuboid,sphere

#Circle
radiusCir = int(input("Enter the radius of the circle"))
print("The Area of the circle is",circle.area(radiusCir))

#Rectangle
length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
print("Area of the rectangle is",rectangle.area(length,breadth))
print("Perimeter of the rectangle is",rectangle.perimeter(length,breadth))

#cuboid
lengthCub = int(input("Enter the length of the cuboid"))
breadthCub = int(input("Enter the breadth of the cuboid"))
heightCub = int(input("Enter the height of the cuboid"))
print("The volume of the cuboid is:",cuboid.volume(lengthCub,breadthCub,heightCub))
print("The perimeter of the cuboid is:",cuboid.perimeter(lengthCub,breadthCub,heightCub))

#sphere
radiusSph = int(input("Enter the radius of the sphere"))
print("The Area of the sphere is:",sphere.area(radiusSph))
