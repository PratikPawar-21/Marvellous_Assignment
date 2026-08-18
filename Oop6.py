class demo:
    
    value1 = 10
    value2 = 20

    def __init__(self):
        self.no1 = 11
        self.no2 = 21

   
obj1 = demo()
obj2 = demo()
obj1.no1 = 0

print(obj1.no1)
print(obj2.no1)

demo.value1 = 0
print(demo.value1)
