#Abstracion is used to hide irrelevant details from the user and show the details that are relevant to the users.

class car:
    def __init__(self):
        self.clutch = False
        self.brk = False
        self.acce = False
        
    def start(self):
        self.clutch = True
        self.acce = True
        print("car started ..")

def main():        
    dr1 = car()
    dr1.start()   

if __name__ == "__main__":
    main()    
