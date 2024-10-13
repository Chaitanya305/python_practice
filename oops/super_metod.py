#super method we will use when we want values to be set or some method of parent should get call after creation of child class object

class car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started ..")
    
    @staticmethod
    def stop():
        print("car stoped ..")
        
class tata(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
        
        
c1=tata("nexon","petrol")
#print(c1.type)  #--> car.type valyue is not yet set or define
print(c1.type)  #--> this is after super method is called
