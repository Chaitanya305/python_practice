class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, or2):
        return self.price > or2.price
    
    
or1= order("juice", 2)

or2 = order("samosa", 10)

print(or2 > or1 )