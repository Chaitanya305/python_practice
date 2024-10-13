class customer:
  def __init__(self,name):
    self.name=name

def greet(customer1):
  customer1.name ="nitish"
  
  print(customer1.name)

cust=customer("sagar")
greet(cust)
print(cust.name)