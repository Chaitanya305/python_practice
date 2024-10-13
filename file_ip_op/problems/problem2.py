with open("number.txt", 'w') as f:
    f.write("1, 2, 45, 55, 86, 76")
    
'''with open("number.txt", 'r') as f:
    data = f.read()
    data = data.split(", ")
    count=0
    for i in data:
        if int(i)%2==0:
            count+=1

print(count)
'''
with open("number.txt", 'r') as f:
    data = f.read()
    print(data)
    
    num=""
    for i in range(len(data)):
        if data[i] == "," or i == (len(data)-1):
            print(num)
            num=""
        elif data[i] == " ":
            continue
        else:
            num=num+data[i]
    
