class Base:

    def fun(self):
        print("inside base fun")

class derived(Base):
    def sun(self):
        print("inside derived sun")

   
        
        
dobj = derived()
dobj.fun()
dobj.sun()

