class Base1:

    def fun(self):
        print("inside base1 fun")

class Base2:

    def gun(self):
        print("inside base2 gun")

class derived(Base1,Base2):
    def sun(self):
        print("inside derived sun")
       
dobj = derived()
dobj.fun()
dobj.gun()
dobj.sun()

