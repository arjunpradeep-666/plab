class Rectangle :
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
l=float(input("enter the length:")) 
b=float(input("enter the breadth:")) 

rect=Rectangle(l,b)
print("area of rectangle:",rect.area())
print("perimeter of rectangle:",rect.perimeter())