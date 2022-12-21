class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth


    def display(self):
        print("Area of the Rectangle = ",(self.length*self.breadth))
        print("Perimeter of the Rectangle = ",(2*(self.length+self.breadth)))

    def returnArea(self):
        return self.length*self.breadth

r11 = int(input("Enter the length of the first rectangle"))
r12 = int(input("Enter the breadth of the first rectangle"))
r21 = int(input("Enter the length of the second rectangle"))
r22 = int(input("Enter the breadth of the second rectangle"))
r1 = Rectangle(r11,r12)
r2 = Rectangle(r21,r22)
r1.display()
r2.display()

if(r1.returnArea() > r2.returnArea()):
    print("Area of r1 is bigger")
else:
    print("Area of r2 is bigger")