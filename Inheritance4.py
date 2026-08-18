class Base:
    def __init__(self):
        print("inside base constructer")

    def fun(self):
        print("inside base fun")

class derived(Base):
    def __init__(self):
        super().__init__()
        print("inside derived constructer")

dobj = derived()
dobj.fun()

