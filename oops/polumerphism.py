#when operator is allowed to have differant meaning according to context
#like + operator has differant mening for 1+2 -->3 "sagar" + "sakshi"  -->sagarsakshi , as per context it has differnt meaning 

#operator overloading means polimerphism --> when you chnage behavior of your operator then it is operator overloading

#eg for __add__() if you chnage its behaviour for you class then it is called operator overloading44

# there are many default dunder function created in pyhton we can use them to get that behaviour for our class

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(f'{self.real} i + {self.img} j')

    def add(self, num2):
        real=self.real + num2.real
        img= self.img + num2.img
        return f'{real} i + {img} j'    
    
    def __add__(self, num2):
        real=self.real + num2.real
        img= self.img + num2.img
        return f'{real} i + {img} j'

#synatx of __add__is 
#  obj1.__add__(self,obj2)    


num1=complex(3,2)
num1.show()
num2=complex(3,4)
num2.show()

#below is he way we can create our own add method
num3=num1.add(num2)
print(num3)

# now do same using operator overloading "+" this is opearator need to used 

num3=num1 + num2
print(num3)

# above will giove error if we dont use opeartor overloading, beacouse he has no idea for complex_obj+complex_obj what he need to do