class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def gender(self):
        print("male")

class student(user):

    def gender(self):
        print("female")

s=student("sagar",23)
s.gender()
    