# a = int(input('one : '))
# b = int(input('two : '))
try:
    #Input is within a error
    a = int(input('one : '))
    b = int(input('two : '))

    print(a/b)

except ValueError:
     print('Invalid Users Input')

#ZeroDivisionError is for if the user divides by 0
except ZeroDivisionError:
    print('nothing can be defines by 0')