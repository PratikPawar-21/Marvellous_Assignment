import time
import threading 

def SumEven(No):

    print("TID of sumeven thread is:",threading.get_ident())

def Sumodd(No):
    
   print("TID of main thread :",threading.get_ident())


def main():
    print("TID of sumodd thread is:",threading.get_ident())

    start_time = time.perf_counter()
    t1 = threading.Thread(target=SumEven,args=(10000000,))
    t2 = threading.Thread(target=SumEven,args=(10000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

    end_time = time.perf_counter()

    print(f"time required is : {end_time - start_time:.5f}second")

if __name__ == "__main__":
    main()