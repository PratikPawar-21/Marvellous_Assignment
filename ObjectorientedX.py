class Arithmatic:

    def Addition(self,no1,no2):
        Ans = no1 + no2
        return Ans 

    def Subtraction(self,no1,no2):
        Ans = no1 - no2
        return Ans 

aobj = Arithmatic()

print("Enter first number:")
value1 = int(input())

print("Enter second number:")
value2 = int(input())

#Ret = Addition(aobj,value1,value2)
Ret = aobj.Addition(value1,value2)  
print("Addition is :",Ret)

Ret = aobj.Subtraction(value1,value2)   
print("Subtraction is :",Ret)

