
def SumEven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

def Sumodd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of odd :",Sum)

def main():
    SumEven(1000000)
    Sumodd(100000)
    

if __name__ == "__main__":
    main()