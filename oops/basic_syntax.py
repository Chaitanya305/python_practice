class calculator:
    sister="sakshi"  #>> this is class variable/static variable can be acces by class name directly eg. calculator.sister or with object eg. object.variable 
    __gender="Male"  #>> this is private variable cant be acces simply by its name
    
    def __init__(self,company):       #>> this is constructor
        print("*********this is calculator program***********")
        self.company=company    #>> variable define by self.var_name are instnace varibale they get differant value for each objects 
        print("this is from ",company, id(company))
        print("accesing class varibale: ",self.sister)
    
    #below one is instance method
    def add(self,a,b):
        self.name="chaitanya"   # data that need to be get acces by other methods in class need to be define using self.data= 
        place="nashik"  # data without self cant be acces by other methods in class  >> thi is local variable having scope for that method only where it defied 
        print(place)
        print(self.company) 
        print("accesing class varibale: ",calculator.sister)
        print("geneder is ",self.__gender)  #private variable are accesibale for its class
        return a+b
    
    
    def mult(self,a,b):
        #varibake from other method can be acces by self object 
        print(self.name)
        try:
            print(self.place)
        except AttributeError:
            print("data is not defined as self.data in other method")
        except Exception as e:
            print("error occured",e)      
        return a*b

    
def main():
    calculator.sister="bhagyashree"  
    ob=calculator("LTI")
    print(ob.sister,calculator.sister)
    print(ob.company)
    #print(ob.name) # this will give error as it is not yet get deifne as add method is not yet called 
    print(ob.add(1,2))
    print(ob.mult(1,2))
    print(ob.name)
    print(ob.company)  # this is acces after function has bee called so will not give error
    #print(ob.place)  it is local var will give attribute error
    print(ob._calculator__gender) #>> in python nothing is truely get hide, it can be acces like this
    class customer:
        def demo(self):
            return ob._calculator__gender
    ob2=customer()
    print(ob2.demo())
    ob3=calculator('LTI')
    print("this is from ob3",ob3.sister)


if __name__ == "__main__":
    main()