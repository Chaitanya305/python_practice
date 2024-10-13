class cart:    
    
    def __init__(self,dict: dict):
        self.dict = dict
         
    def add_item(self, item, price):
        self.dict[item]=price
                
    def remove_item(self,item):
        del self.dict[item]  
    
    def cal_price(self):
        price = 0
        for value in self.dict:
            price = price + self.dict[value]
        print(price)
    
    
user1 = cart({})
user1.add_item("chips", 10)
user1.add_item("samosa", 20)
user1.cal_price()
user1.remove_item("samosa")
user1.cal_price()

user2 = cart({})
user2.add_item("kachori", 20)
user2.add_item("samosa", 20)
user2.cal_price()
user2.remove_item("samosa")
user2.cal_price()
