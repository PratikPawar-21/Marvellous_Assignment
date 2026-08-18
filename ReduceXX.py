from functools import reduce 

checkEven = lambda n:(n % 2 == 0)

Inc = lambda n : n+1

Add = lambda n1, n2 :n1 + n2

def main():
    data = [13,12,8,9,10,11,20]
    print("Input Data is :",data)

    fdata = list(filter(checkEven,data))
    print("data after filter :",fdata)

    mdata = list(map(Inc,fdata))
    print("data after map :",mdata)

    rdata = reduce(Add,mdata)
    print("data after reduce :",rdata)

if __name__ == "__main__" :
    main()