class percentage:
  def __init__(self,m1,m2,m3):
    self.m1=m1
    self.m2=m2
    self.m3=m3
    #self.get_percentage = (self.m1+self.m2+self.m3)/3
  
  @property
  def cal_percentage(self):
    return (self.m1+self.m2+self.m3)/3
   
  #def cal_percentage(self):                      -->this will also works same only
  #  return (self.m1+self.m2+self.m3)/3


stu1=percentage(90,98,94)
#print(stu1.get_percentage)
stu1.m2=94
#print(stu1.get_percentage)   this will still print percentage with old marks
print(stu1.cal_percentage)    #This will update percentange with updated marks