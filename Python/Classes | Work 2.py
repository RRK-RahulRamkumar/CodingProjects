class Shape:
    def __init__(self):
        self.__areaValue = 0
        self.__perimeterValue = 0

    def area(self):
        print(f"Area value is {self.__areaValue}")

    def perimeter(self):
        print(f"Perimeter value is {self.__perimeterValue}")

class rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def area(self):
        print(f"Area of rectangle is {self.__length * self.__breadth}")

    def perimeter(self):
        print(f"Perimeter of rectangle is {2 * (self.__length + self.__breadth)}")

class circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        print(f"Area of circle is {3.14 * (self.__radius ** 2)}")
    
    def perimeter(self):
        print(f"Perimeter of circle is {2 * 3.14 * self.__radius}")

myCircle = circle(20)
myCircle.area()
myCircle.perimeter()

myRectangle = rectangle(10, 17)
myRectangle.area()
myRectangle.perimeter()
