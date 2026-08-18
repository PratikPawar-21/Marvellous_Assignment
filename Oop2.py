class demo:
    
    value1 = 10
    value2 = 20

    def __init__(self):
        self.no1 = 11
        self.no2 = 21

    # instance method
    def fun(self):
        print("inside instance method named as fun")
        print(self.no1)
        print(self.no2)
        print(demo.value1)
        print(demo.value2)

dobj = demo()
dobj.fun()