import time 
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
    start_time = time.perf_counter()
    SumEven(1000000)
    Sumodd(100000)
    
    end_time = time.perf_counter()

    print(f"time required is : {end_time - start_time:.5f}second")

if __name__ == "__main__":
    main()