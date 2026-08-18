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

    except ValueError as vobj:
        print("Exception occur due to invlid data type :",vobj)

    except Exception as eobj:
        pritn("Exception occur :",eobj)

    finally:
        print("inside finally block")


    print("result is :",Ans)

if __name__ == "__main__":
    main()