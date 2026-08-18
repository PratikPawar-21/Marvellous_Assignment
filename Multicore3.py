import time


def SumCube(no):
    Sum = 0

    for i in range(1,no+1):
        Sum = Sum +(i ** 3)
    return Sum


def main():
    Data = [10000000,20000000,30000000,40000000,50000000]

    Result = []

    star_time = time.perf_counter()

    for value in Data:
        Ret = SumCube(value)
        Result.append(Ret)

    end_time = time.perf_counter()

    print("Result is :")
    print(Result)
    

    print(f"time required {end_time - star_time}")
    

if __name__ == "__main__":
    main()