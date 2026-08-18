class Base:
    def __init__(self):
        print("inside base constructer")

class derived(Base):
    def __init__(self):
        super().__init__()
        print("inside derived constructer")

bobj = derived()

