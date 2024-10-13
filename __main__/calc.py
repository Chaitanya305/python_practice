class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mult(self):
        return self.a*self.b


def main(): 
    print("this is clalculatior class")

if __name__ == "__main__":
    main()
