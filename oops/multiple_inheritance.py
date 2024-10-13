class a:
    a="this is form class a"
    
class b:
    b="this is form class b"
    
class c(a, b):
    c="this is from class c"
    
ob=c()  #object c class created
print(ob.a)  # it can acces both a and b class as c class is taking properties and methods form both a and b class
print(ob.b)
print(ob.c)