from datetime import date

class person:
    current_year = date.today()
    
    def __init__(self,name,country,dob):
        self.name = name
        self.country= country
        self.dob = dob   
        
    def get_age(self):
        return person.current_year.year - self.dob
        
p1= person("chaitanya", "india", 2000) 
print(p1.get_age())
p2=person("sakshi", "dhule", 2001)
print(p2.get_age())