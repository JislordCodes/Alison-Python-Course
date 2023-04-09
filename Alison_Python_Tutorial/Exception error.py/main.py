"""try:
    a = int(input('~'))
except Exception:#Exception represent errors in python
    print('User Error')#Print this instead of running our file

try:
    a = int(input('~'))
except Exception as error:#error here is a variable in exception error and were using that for description of the problem
    print('User Error:' + str(error))#Print this instead of running our file

custom exception for each error
try:
    a = int(input('~'))

#Specific Error
except ValueError:#Value error
    print('Invalid user input')#Print this instead of running our file
except TypeError:#type error
    print('type error')
except KeyboardInterrupt:
    print('keyboard Interupt')
"""

#secure file
try:
    print('opened file')
    a = int(input('~'))

#Specific Error
except ValueError:#Value error
    print('Invalid user input')#Print this instead of running our file
except TypeError:#type error
    print('type error')
except KeyboardInterrupt:
    print('keyboard Interupt')

finally: #Execute even is the user gives wrong input, you have to close the file or database
    print('closed file')