class xyx:
    def area(self,a,b=0):
        if b==0:
            print(f"area of circle is {a*3.14:.2f}")

        else:
            print("area of rectangle is ",a*b)

ob=xyx()
ob.area(10)
ob.area(10,20)