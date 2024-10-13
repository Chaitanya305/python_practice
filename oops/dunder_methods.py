class complex_add:
    def __init__(self,real,imag):
        self.real= real
        self.imag = imag
    
    def add(self,num):
        real = self.real + num.real
        imag = self.imag + num.imag
        return f'{real}i + {imag}j' 
    
    def __add__(self,num):
        real = self.real + num.real
        imag = self.imag + num.imag
        return f'{real}i + {imag}j' 
       
  #  def __add__(self):
  #      return     
  
num1=complex_add(3,5)
num2= complex_add(4,5)
num3 = num1.add(num2)   # this is define how add should be done in for our class but this thing didnt define how '+' operator should work for our class objects
print(num3)
num3 = num1 + num2      # this + how need to work for our object is we define using dunder mthod __add__ 
print(num3)
print(num1 + num2)