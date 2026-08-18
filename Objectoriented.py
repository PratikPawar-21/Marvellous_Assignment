class Arithmatic:

    def Addition(no1,no2):
        Ans = no1 + no2
        return Ans 

    def Subtraction(no1,no2):
        Ans = no1 - no2
        return Ans 

aobj = Arithmatic()

print("Enter first number:")
value1 = int(input())

print("Enter second number:")
value2 = int(input())

Ret = aobj.Addition(value1,value2)  # Error
print("Addition is :",Ret)

Ret = aobj.Subtraction(value1,value2)   #Error
print("Subtraction is :",Ret)

