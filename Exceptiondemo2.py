def main():
    Ans = 0

    try:
        print("Enteer first number :")
        No1 = int(input())

        print("Enteer second number :")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successful")

    except ZeroDivisionError as zobj:
        print("Exception occur due to second opperand is zero :",zobj)

    print("result is :",Ans)

if __name__ == "__main__":
    main()