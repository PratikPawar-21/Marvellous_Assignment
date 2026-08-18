class demo:
    def __init__(self,A):
        self.no = A

    def __add__(self,other):
       return self.no + other.no

    def __sub__(self,other):
        return self.no - other.no

    def __mul__(self,other):
        return self.no * other.no

    def __truediv__(self,other):
        return self.no / other.no


obj1 = demo(11)
obj2 = demo(21)

print(obj1 + obj2) #0bj1.__add__(obj2) -> __add__(obj1,obj2)
print(obj1-obj2)   #0bj1.__sub__(obj2) -> __sub__(obj1,obj2)
print(obj1*obj2)   #0bj1.__mul__(obj2) -> __mul__(obj1,obj2)
print(obj1/obj2)   #0bj1.__truediv__(obj2) -> __div__(obj1,obj2)
