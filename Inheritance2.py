class Base:
    def __init__(self):
        print("inside base constructer")

class derived(Base):
    def __init__(self):
        print("inside derived constructer")

bobj = Base()

