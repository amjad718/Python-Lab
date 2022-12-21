class Rectangle:

    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        self.area = self.__length * self.__width

    def __lt__(self,other):
        return self.area < other.area



a = int(input("Enter length of first rectange : "))
b = int(input("Enter width of first rectangle : "))
c = int(input("Enter length of second rectangle : "))
d = int(input("Enter width of second rectangle : "))


rect1 = Rectangle(a,b)
rect2 = Rectangle(c,d)

if(rect1 < rect2):
    print("Area of rectangle 2 is greater")
else :
    print("Area of rectangle one is greater")