import os
import time
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} ppid of SumEven :{os.getppid()}")
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

def Sumodd(No):
    print(f"PID of Sumodd : {os.getpid()} ppid of Sumodd :{os.getppid()}")
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of odd :",Sum)

def main():
    print(f"PID of main : {os.getpid()} ppid of main :{os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven,args=(10000000,))
    t2 = multiprocessing.Process(target=Sumodd,args=(10000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

    end_time = time.perf_counter()

    print(f"time required is : {end_time - start_time:.5f}second")

if __name__ == "__main__":
    main()