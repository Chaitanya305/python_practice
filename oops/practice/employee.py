class employe:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showdetails(self):
        print("role is ",self.role)
        print("department is ",self.department)
        print("salary is ",self.salary)
        

class engineer(employe):
    def __init__(self, name, age):
        super().__init__("enginerr", "it", "60,000")
        self.name = name
        self.age = age

emp1=employe("GT", "cis", 20000)
emp1.showdetails()
    
emp2=engineer("chaitanya", 24)
print(emp2.name)
emp2.showdetails()
