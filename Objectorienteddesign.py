class Arithmatic:

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B


    def Addition(self):
        Ans = self.no1 + self.no2
        return Ans 

    def Subtraction(self):
        Ans = self.no1 - self.no2
        return Ans 



print("Enter first number:")
value1 = int(input())

print("Enter second number:")
value2 = int(input())

aobj = Arithmatic(value1,value2)

#Ret = Addition(aobj,value1,value2)
Ret = aobj.Addition()  
print("Addition is :",Ret)

Ret = aobj.Subtraction()   
print("Subtraction is :",Ret)

