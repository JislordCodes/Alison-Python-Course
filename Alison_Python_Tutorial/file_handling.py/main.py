"""Variables go away when code is not running... storing in a file will be helpful"""
 
#r here is for reading
with open('file_handling.py\data.txt','r') as file:
    data = file.read()
    print(data)


#read 1st 4 characters
with open('file_handling.py\data.txt','r') as file:
    data = file.readline(4)
    print(data)

#return each lines as an elements of the list
with open('file_handling.py\data.txt','r') as file:
    data = file.readlines()
    print(data)