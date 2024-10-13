from calc import calculator,main   # evenr afterimporting only class calculator from calc is still printing statement outside the class

ob = calculator(10,12)
print(ob.add())
print(ob.mult())
print(ob.sub())
main()  # this is printing pritn statment now only becouse main is also imported,

'''if we use 

from calc import calculator   

ob = calculator(10,12)
print(ob.add())
print(ob.mult())
print(ob.sub())


in this case print statement will not come.
'''