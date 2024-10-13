with open("practice.txt","w") as f:
    f.write("this is file written by python\ni love python\n")
    f.write("i am cloud engineer\nwe are learning file i/o in python")

with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
data = data.replace("python", "java")

with open("practice.txt","w") as f:
    f.write(data)
    
with open("practice.txt","r") as f:
    data=f.read()
    if "cloud" in data:
        print("found")
    else:
        print("not_found")
        
'''def find_line():
    word = "chaitanya"
    with open("practice.txt") as f:
        count = 1
        line = f.readline()
        while(len(line)!=0):
            if word in line:
                print(count)
                print(f'{word} is found at {count}')
                break
            line = f.readline()
            count+=1
        else:
            print(-1)
    

find_line()
'''

def find_line():
    word = "chaitanya"
    data = True
    count=1
    with open ("practice.txt") as f:
        while (data):
            data = f.readline()
            if (word in data):
                return count
            count+=1
    return -1 

print(find_line())