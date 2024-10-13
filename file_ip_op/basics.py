f = open("hello.txt","rt")   # r is default mode for open file, mode can be called combine also

#data = f.read()  # once file is completly get read, cursore will go at end of file which is empty so for next read or readline it will print blanck space 
#print(data)

s1=f.readline()     # it will read first line with /n and then cusrose will be at second line
print(s1)   # s is string it read all lines and stored all as string in one variable

s2= f.readline()  # now cursore will read second line as it is on second line and goes to third line, which is blank space.
print(s2)

s3=f.readline()   #this will print blank space as no data in the file present at third line as our cursore now gone to third line
print(s3)

'''modes
r - read 
w - write  -- here also if file not exist will be get created
x - create new file and write data into it
a - append to the file -- here also if file not exist will be get created
b - binary mode to open binary file 
t - to open text file  ---> this is also default like read
+ - to open file for reading and writing -->like eg r+ --> read and write, w+ --> write and read, a+ --> write and read
'''

#read() --> it read entire file data as string, param pass to method is will read only that much char of string
#readline() --> it read the file line by line and store it as string, param pass to method is will read only that much char of string 
#readlines()  --> it reads all line of file and store in list of string, where each line as string.

#s1 = f.read(5)  # read only first 5 letters
#print(s1)

#line1 = f.readline()
#print(line1) 