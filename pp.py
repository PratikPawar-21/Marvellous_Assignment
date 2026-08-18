def min(data):
    sum = 0
    
    for i in data:
        sum = sum + i
    
    return sum

def main():
    no = int(input("Enter a Number :"))

    List = []

    print("Enter elements : ")

    for i in range (no):
        Num = int(input())
        List.append(Num)

    ret = min(List)
    
    print("minimum of all elements : ",ret)


if __name__ == "__main__":
    main()