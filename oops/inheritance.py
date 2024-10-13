#when one class (child) derives the properties and methods of another class(parent) that is called inheritance

class car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped..")    
        
        
class tata(car):
    brnad = "Tata"
    def __init__(self,name):
        self.name = name
    
c1=tata("nexon")
print(c1.name)
c1.start()   # due to inheritance all parent class attribute methods are now accesible to tata object also