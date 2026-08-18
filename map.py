def checkEven(n):
    return (n % 2 == 0)


def Inc(n):
    return n+1


def main():
    data = [13,12,8,10,11,20]
    print("Input Data is : ",data)
     
    fdata = list(filter(checkEven,data))
    print("data after map : ",fdata)

    mdata = list(map(Inc,fdata))
    print("Data after map : ",mdata)


if __name__ == "__main__":
    main()
    
