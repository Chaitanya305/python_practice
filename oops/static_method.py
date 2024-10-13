# static methods are used when you dont need self, self is what it is nothing but pointing to same object/instnace from which it is getting called 
#static varibale it is used when you know it wont be changing for each instnace, when you want var to be constant for all object/instnace in such case we use static/class varibale


from basic_syntax import calculator

cal=calculator("LTI")
cal.add(1,2)

class student:
    school = "maratha highschool"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("student name is ",self.name)
        name="sakshi"
        print(name)
        print("student age is ",self.age)
        print("name of school is ",student.school)
        student.school="pethe"
        print(student.school)
    
    def display(self):
        print("this is name from display",self.name)
    
    @staticmethod            #static cmethod cant acces instnace varibale it can only acces static var
    def principle():
        name="chaitanya"
        print("name of school in static method ",student.school)
        student.school="pethe"
        print(student.school)
        
    @classmethod    # this are the methods use to acces class var/ststic var  this is usually use to make changes in static var
    def get(cls,school_name):
        cls.school=school_name

ob=student("chaitanya",22)

ob.show()
#ob.principle() this is not good practice 
student.principle()
ob.display()
        
student.get("kthm")