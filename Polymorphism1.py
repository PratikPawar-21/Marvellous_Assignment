class base:
    def fun(self):
        print("inside base fun")

class derived(base):
    def fun(self):
        print("inside derived fun")

dobj = derived()
dobj.fun()

